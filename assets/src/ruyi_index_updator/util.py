"""
Utils
"""

import atexit
import tempfile
import shutil

from awesomeversion import AwesomeVersion

from ..matrix_parser import SystemInfo, SystemIdentifier


def folder_tmp_mux(folder: str | None) -> str:
    """
    If the folder is None, return a tmp folder.

    Clean the tmp folder if created.

    A special usage is to use it as a automatiaclly clean tmp folder **after** the program ends,
    as tmpfile only gives this ability in the context manager.
    """
    p = folder if folder is not None else tempfile.mkdtemp()

    def __release_tmp_path():
        shutil.rmtree(p)
    if folder is None:
        atexit.register(__release_tmp_path)
    return p


def cmp_version(ver1: str, ver2: str) -> int:
    """
    Compare the version
    """
    av1 = AwesomeVersion(ver1)
    av2 = AwesomeVersion(ver2)
    if av1 > av2:
        return 1
    if av1 < av2:
        return -1
    return 0


def board_id(info: SystemInfo | SystemIdentifier) -> str:
    """
    Return the board id
    """
    return info.vendor


def board_variants(info: SystemInfo | SystemIdentifier) -> list[str]:
    """
    Return the board variants
    """
    if info.board_variants is None:
        return ['generic']
    return info.board_variants


def system_id(info: SystemInfo | SystemIdentifier, variant: str | None) -> str:
    """
    Return the system id
    """
    # This map should be removed.
    # But some changes in packages-index is needed.
    # So we need to keep it for now.
    system = info.system
    if system == 'openeuler':
        system = 'oerv'

    if variant is None or variant == 'generic':
        return f"{system}-{info.vendor}"

    return f"{system}-{info.vendor}-{variant}"
