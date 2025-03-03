# pylint: disable=import-outside-toplevel, missing-function-docstring, missing-module-docstring, wildcard-import, unused-wildcard-import, missing-class-docstring
"""
To use simple getter, here are a few restrictions:
1. The device should have no variant (i.e.: only generic)
2. Only one image file for each release
"""

from typing import Optional, TypedDict, Required, Protocol

from .prelude import *

__version__ = "1.0.0"


class FilterDecl(TypedDict):
    type: Optional[Literal["regex", "lambda"]]  # Default to "regex"

    # if type is "lambda", this should be the lambda function
    #       lambda should be like:
    #           def lambda_func(name: str, info: SystemInfo) -> bool
    # if type is "regex", this should be a regex tester, given a name only
    filter: Required[str]


class MapperDecl(TypedDict):
    type: Optional[Literal["regex", "lambda"]]  # Default to "regex"
    regex: Optional[str]

    # if type is "lambda", this should be the lambda function
    #       lambda should be like:
    #           def lambda_func(name: str, info: SystemInfo) -> str
    # if type is "regex", this should be a format string,
    #     format args is the regex groups
    mapper: Required[str]


class InfoDecl(TypedDict):
    id: Optional[str]
    vendor: Required[str]
    system: Required[str]
    variant: Required[str]

    repo: Required[str]

    # To map the github release to the system version
    release_filter: Required[FilterDecl]

    # To map the system version to a symver
    version_mapper: Required[MapperDecl]

    # filter the file name
    asset_filter: Required[FilterDecl]

    strategy: Optional[str]  # Default to "dd_v1"

    partition_map: Optional[str]  # In simple, only one file. Default to "disk"

    # For the description of the system
    # This doesn't follow the original MapperDecl design
    # If the type is "lambda", this should be the lambda function
    #      A SystemInfo will be passed to the lambda, return a str
    # If the type is "regex", this should be a format string,
    #      format args is a SystemInfo object named "info"
    #      eg: "System {info.system} as {info.variant}"
    desc_mapper: Required[MapperDecl]

    # Optional: generate display name for the system
    # If not provided, a default name will be generated
    # Defination is the same as desc_mapper
    name_mapper: Optional[MapperDecl]


class GithubReleaseGetter(UploadPluginBase):

    handler_lst: list[InfoDecl]

    def __init__(self):
        super().__init__()
        self.handler_lst = []
        for i in config["plugin_cfg"]["handler"]:
            self.logger.info("III %s %s", i["plugin"], i["id"])
            if i["plugin"] == self.get_name():
                self.logger.info("Github Release Simple loads: %s", i["id"])
                self.handler_lst.append(i)

    @staticmethod
    def get_name() -> str:
        return "github_release_simple"

    def __gen_ident(self, info: InfoDecl) -> SystemIdentifier:
        return self.SystemIdentifier(
            vendor=info["vendor"],
            system=info["system"],
            variant=info["variant"]
        )

    def all_can_handle(self):
        res = []

        for handler in self.handler_lst:
            res.append(self.__gen_ident(handler))
        return res

    def system_display_name(self, info, variant=None):
        for handler in self.handler_lst:
            if self.__gen_ident(handler) != info:
                continue
            if handler.get("name_mapper") is not None:
                if handler["name_mapper"]["type"] == "lambda":
                    func = eval(handler["name_mapper"]["mapper"])
                    return func(info, variant)
                else:
                    return handler["name_mapper"]["mapper"].format(info=info)
        return f"{info.system} {info.variant or ''} for {info.product}"

    def system_image_files(self, info, variant=None):
        res = []
        for handler in self.handler_lst:
            if self.__gen_ident(handler) != info:
                continue
            name = self.util.system_id(info, variant)
            res.append(name)
        return res

    def handle_version(self, info):
        for handler in self.handler_lst:
            if self.__gen_ident(handler) != info:
                continue
            if handler["version_mapper"]["type"] == "lambda":
                func = eval(handler["version_mapper"]["mapper"])
                return func(info)
            else:
                r = handler["version_mapper"]["regex"]
                m = self.re.findall(r, info.version)
                return handler["version_mapper"]["mapper"].format(*m)
        raise RuntimeError(f"No handler found for {info}")

    def __fetch_release(self, info: SystemInfo, handler: InfoDecl):
        api_url = f"https://api.github.com/repos/{handler['repo']}/releases"
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "X-Github-API-Version": "2022-11-28",
        }
        response = self.requests.get(api_url, headers=headers, timeout=10)

        if response.status_code != 200:
            raise ValueError(f"Failed to fetch release info: {response.text}")
        releases = response.json()
        for release in releases:
            if handler["release_filter"]["type"] == "lambda":
                func = eval(handler["release_filter"]["filter"])
                if func(release["name"], info):
                    return release
            else:
                if self.re.search(handler["release_filter"]["filter"], release["name"]):
                    return release
        raise ValueError("No release found")

    def __extract_download_asset(self, info: SystemInfo, handler: InfoDecl, gh_release):
        assets = gh_release["assets"]
        for asset in assets:
            if handler["asset_filter"]["type"] == "lambda":
                func = eval(handler["asset_filter"]["filter"])
                if func(asset["name"], info):
                    return asset
            else:
                if self.re.search(handler["asset_filter"]["filter"], asset["name"]):
                    return asset
        raise ValueError("No download url found in release")

    def __gen_desc(self, info, handler):
        if handler["desc_mapper"]["type"] == "lambda":
            func = eval(handler["desc_mapper"]["mapper"])
            return func(info, info.variant)
        else:
            return handler["desc_mapper"]["mapper"].format(info=info)

    def handle_report(self, info):
        for handler in self.handler_lst:
            if self.__gen_ident(handler) != info:
                continue
            release = self.__fetch_release(info, handler)
            asset = self.__extract_download_asset(info, handler, release)
            img_path = self.os.path.join(
                self.__tmppath__, asset["name"]
            )
            img_file = self.download_file(
                img_path, asset["browser_download_url"])
            img_dist = self.gen_distfile(
                img_file, asset["browser_download_url"])
            desc = self.__gen_desc(info, handler)
            partition_map = handler.get("partition_map", "disk")
            partition_map = {
                partition_map: self.util.system_id(info, None)
            }
            generator = self.BoardImagesGenerator(
                version=self.handle_version(info),
                desc=desc,
                vendor=info.vendor,
                distfiles=[img_dist],
                strategy=handler.get("strategy", "dd_v1"),
                partition_map=partition_map,
                status=info.raw_data.status
            )
            return {
                self.util.system_id(info, None): generator
            }

        raise RuntimeError(f"No handler found for {info}")


def register() -> UploadPluginBase | None:
    return GithubReleaseGetter()
