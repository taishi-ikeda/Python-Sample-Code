from . import search_base as sb
from . import search_sequential as ss
from . import search_sequential_sort as sss
from . import search_mblock as smb
from . import search_binary as sbi

class search_factory:
    __slots__ = ()

    @classmethod
    def create(cls, x: str, verbose: bool = False) -> sb.search_base:
        if x == "sequential":
            return ss.sequential_search(verbose)
        elif x == "sequential_sort":
            return sss.sequential_sort_search(verbose)
        elif x == "mblock":
            return smb.mblock_search(verbose)
        elif x == "binary":
            return sbi.binary_search(verbose)
        else:
            print("error:unknown method : ", x)
            exit(-1)
