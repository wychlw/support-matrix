# pylint: disable=import-outside-toplevel, missing-function-docstring, missing-module-docstring, wildcard-import, unused-wildcard-import, missing-class-docstring
# pylint: disable=eval-used
from typing import Optional, TypedDict, Required

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


class FileDecl(TypedDict):
    # Just used as an identifier of a file in logging, not necessary
    id: Optional[str | None]

    # Which fileset does this file belongs to
    fileset: Required[list[str] | None]

    # The given str is the vinfo.version
    url: Optional[MapperDecl]

    # To filter a file name
    file_filter: Required[FilterDecl]

    partition_map: Optional[str]  # Default to "disk"

# Settings in here override the global repo setting


class FileSetDecl(TypedDict):
    """
    Fileset is a list of files using in a single image_combo,
    for example: boot part and root part for a fastboot img
    """

    # The id to seperate each file set, will be appended to the end of the image-combo
    # Can be null, but only one id null file is allowed
    id: Required[str | None]

    prepend: Optional[str]
    append: Optional[str]

    board_variants: Required[list[str] | None]

    desc_mapper: Optional[MapperDecl]


class InfoDecl(TypedDict):
    id: Optional[str]
    vendor: Required[str]
    board_variants: Optional[list[str] | None]
    system: Required[str]
    variant: Required[str]

    # The given str is the vinfo.version
    url: Optional[MapperDecl]

    # To map the system version to a symver
    version_mapper: Required[MapperDecl]

    fileset: Required[list[FileSetDecl]]
    files: Required[list[FileDecl]]

    strategy: Optional[str]  # Default to "dd_v1"

    # Optional: generate display name for the system
    # If not provided, a default name will be generated
    # Defination is the same as desc_mapper
    name_mapper: Optional[MapperDecl]


class MirrorsiteGetter(UploadPluginBase):

    handler_lst: list[InfoDecl]

    def __init__(self):
        super().__init__()
        self.handler_lst = []
        for i in config["handler"]:
            if i["plugin"] == self.get_name():
                _id = i.get(
                    "id", f"{i["system"]}-{i["vendor"]}{f"-{i["variant"]}" if i["variant"]
                                                        != "null" else ""}"
                )
                self.logger.info("Github Release std loads: %s", _id)
                self.handler_lst.append(i)
        for i in self.load_sep_config():
            if i.get("handler", None) is None:
                continue
            for j in i["handler"]:
                if j.get("plugin", None) != self.get_name():
                    continue
                _id = j.get(
                    "id", f"{j["system"]}-{j["vendor"]}{f"-{j["variant"]}" if j["variant"]
                                                            != "null" else ""}"
                )
                self.logger.info("Github Release std loads: %s", _id)
                self.handler_lst.append(j)

    @staticmethod
    def get_name() -> str:
        return "mirrorsite_getter_std"

    def __gen_ident(self, info: InfoDecl) -> SystemIdentifier:
        return self.SystemIdentifier(
            vendor=info["vendor"],
            system=info["system"],
            variant=info["variant"]
        )

    def __match_board_variant(self, board_variant: str | None, handler: InfoDecl) -> bool:
        if board_variant is None or handler["board_variants"] is None:
            return True
        if board_variant in handler["board_variants"]:
            return True
        return False

    def __match_file_set(self, board_variant: str | None, fileset: FileSetDecl) -> bool:
        if board_variant is None or fileset["board_variants"] is None:
            return True
        if board_variant in fileset["board_variants"]:
            return True
        return False

    def __all_file_in_fileset(self, handler: InfoDecl, fileset: FileSetDecl) -> list[FileDecl]:
        res = []
        for file in handler["files"]:
            if fileset["id"] is None or file["fileset"] is None:
                res.append(file)
                continue
            if fileset["id"] in file["fileset"]:
                res.append(file)
                continue
        return res

    def all_can_handle(self):
        res = []
        for handler in self.handler_lst:
            res.append(self.__gen_ident(handler))
        return res

    def system_display_name(self, info, board_variant=None):
        for handler in self.handler_lst:
            if self.__gen_ident(handler) != info or \
                    not self.__match_board_variant(board_variant, handler):
                continue
            if handler.get("name_mapper") is not None:
                if handler["name_mapper"].get("type") is None or \
                        handler["name_mapper"]["type"] == "regex":
                    return handler["name_mapper"]["mapper"].format(info=info)
                elif handler["name_mapper"]["type"] == "lambda":
                    func = self.eval(handler["name_mapper"]["mapper"])
                    return func(board_variant, info)
                else:
                    raise ValueError("Unknown MapperDecl type")
        return f"{info.system} {info.variant or ''} for {info.product}"

    def system_image_files(self, info, board_variant=None):
        res = []
        for handler in self.handler_lst:
            if self.__gen_ident(handler) != info or \
                    not self.__match_board_variant(board_variant, handler):
                continue
            for fileset in handler["fileset"]:
                if not self.__match_file_set(board_variant, fileset):
                    continue
                prepend=fileset.get("prepend")
                append=fileset.get("append")
                name=self.util.file_id(
                    info, board_variant, prepend, append
                )
                res.append(name)
        return self.unique_list(res)

    def __handle_version(self, info: SystemInfo, handler: InfoDecl) -> str:
        if handler["version_mapper"].get("type") is None or \
                handler["version_mapper"]["type"] == "regex":
            r=handler["version_mapper"]["regex"]
            m=self.re.findall(r, info.version)
            return handler["version_mapper"]["mapper"].format(*m)
        elif handler["version_mapper"]["type"] == "lambda":
            func=self.eval(handler["version_mapper"]["mapper"])
            return func(info.version, info)
        else:
            raise ValueError("Unknown MapperDecl type")

    def handle_version(self, info):
        for handler in self.handler_lst:
            if self.__gen_ident(handler) != info:
                continue
            return self.__handle_version(info, handler)
        raise RuntimeError(f"No handler found for {info}")

    def __get_one_page(self, info: SystemInfo, handler: InfoDecl, file: FileDecl):
        if file.get("url") is not None:
            url=file["url"]
        elif handler.get("url") is not None:
            url=handler["url"]
        else:
            raise ValueError(f"No url found for {info} in file {file["id"]}")
        if url.get("type") is None or \
                url["type"] == "regex":
            r=url["regex"]
            m=self.re.findall(r, info.version)
            return url["mapper"].format(*m)
        elif url["type"] == "lambda":
            func=self.eval(url["mapper"])
            return func(info.version, info)
        else:
            raise ValueError("Unknown MapperDecl type")

    import bs4

    def __get_one_mirrorsite_asset(self, info: SystemInfo, handler: InfoDecl, file: FileDecl):
        page_url=self.__get_one_page(
            info, handler, file
        )
        html=self.requests.get(page_url, timeout=60).text
        soup=self.bs4.BeautifulSoup(html, "html5lib")

        hyperlinks=soup.select('a')
        for link in hyperlinks:
            if not link.has_attr("href"):
                continue
            file_link=self.urljoin(
                page_url, str(link["href"]))
            file_name=self.urlbasename(file_link)
            if file["file_filter"].get("type") is None or \
                    file["file_filter"]["type"] == "regex":
                if self.re.search(file["file_filter"]["filter"], file_name):
                    return file_link
            elif file["file_filter"]["type"] == "lambda":
                func=self.eval(file["file_filter"]["filter"])
                if func(file_name, info):
                    return file_link
            else:
                raise ValueError("Unknown FilterDecl type")
        raise ValueError(
            f"No download file found in page {page_url} for {info} with {file['id']}"
        )

    def __gen_desc(self, info: SystemInfo, fileset: FileSetDecl) -> str:
        if fileset.get("desc_mapper") is None:
            return f"{info.system} {info.variant or ''} for {info.product} with version {info.version}"
        if fileset["desc_mapper"].get("type") is None or \
                fileset["desc_mapper"]["type"] == "regex":
            return fileset["desc_mapper"]["mapper"].format(info=info)
        elif fileset["desc_mapper"]["type"] == "lambda":
            func=self.eval(fileset["desc_mapper"]["mapper"])
            return func(info)
        else:
            raise ValueError("Unknown MapperDecl type")

    def __handle_one_variant(self, info: SystemInfo,
                             handler: InfoDecl,
                             board_variant: str) -> dict[str, BoardImagesGenerator]:
        res={}
        for fileset in handler["fileset"]:
            if not self.__match_file_set(board_variant, fileset):
                continue
            distfiles=[]
            partition_map={}
            files=self.__all_file_in_fileset(handler, fileset)
            for file in files:
                img_url=self.__get_one_mirrorsite_asset(info, handler, file)
                img_name=self.urlbasename(img_url)
                img_path=self.os.path.join(
                    self.__tmppath__, img_name
                )
                img_file=self.download_file(
                    img_path, img_url
                )
                img_dist=self.gen_distfile(
                    img_file, img_url
                )
                img_partition=file.get("partition_map", "disk")
                distfiles.append(img_dist)
                partition_map[img_partition]=self.util.remove_file_extension(
                    img_name)
            desc=self.__gen_desc(info, fileset)
            generator=self.BoardImagesGenerator(
                version=self.__handle_version(info, handler),
                upstream_version=info.version,
                desc=desc,
                vendor=info.vendor,
                distfiles=distfiles,
                strategy=handler.get("strategy", "dd_v1"),
                partition_map=partition_map,
                status=info.raw_data.status
            )

            # If a fileset can handle lots of variant, board_variant is no need as it will generate duplicate files
            if fileset["board_variants"] is None or len(fileset["board_variants"]) > 1:
                use_board_variant=None
            else:
                use_board_variant=board_variant
            prepend=fileset.get("prepend")
            append=fileset.get("append")
            res[
                self.util.file_id(info, use_board_variant, prepend, append)
            ]=generator
        return res

    def handle_report(self, info):
        res={}
        for handler in self.handler_lst:
            if self.__gen_ident(handler) != info:
                continue
            if handler["board_variants"] is not None and \
                    len(handler["board_variants"]) > 0:
                board_variants=handler["board_variants"]
            else:
                board_variants=["generic"]
            for board_variant in board_variants:
                new_res=self.__handle_one_variant(
                    info, handler, board_variant)
                for k, v in new_res.items():
                    if res.get(k) is not None:
                        self.logger.warning("Duplicate key: %s", k)
                        continue
                    res[k]=v
        if len(res) <= 0:
            raise RuntimeError(f"No handler found for {info}")
        return res


def register() -> UploadPluginBase | None:
    return MirrorsiteGetter()
