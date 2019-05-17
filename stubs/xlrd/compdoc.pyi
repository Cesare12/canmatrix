# Stubs for xlrd.compdoc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .timemachine import *
from typing import Any

SIGNATURE: bytes
EOCSID: int
FREESID: int
SATSID: int
MSATSID: int
EVILSID: int

class CompDocError(Exception): ...

class DirNode:
    DID: Any = ...
    logfile: Any = ...
    name: Any = ...
    children: Any = ...
    parent: int = ...
    tsinfo: Any = ...
    def __init__(self, DID: Any, dent: Any, DEBUG: int = ..., logfile: Any = ...) -> None: ...
    def dump(self, DEBUG: int = ...) -> None: ...

class CompDoc:
    logfile: Any = ...
    DEBUG: Any = ...
    mem: Any = ...
    sec_size: Any = ...
    short_sec_size: Any = ...
    mem_data_secs: Any = ...
    mem_data_len: Any = ...
    SAT: Any = ...
    dirlist: Any = ...
    SSCS: str = ...
    SSAT: Any = ...
    def __init__(self, mem: Any, logfile: Any = ..., DEBUG: int = ...) -> None: ...
    def get_named_stream(self, qname: Any): ...
    def locate_named_stream(self, qname: Any): ...

def x_dump_line(alist: Any, stride: Any, f: Any, dpos: Any, equal: int = ...) -> None: ...
def dump_list(alist: Any, stride: Any, f: Any = ...) -> None: ...
