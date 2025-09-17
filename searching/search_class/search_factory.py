from . import search_base as sb
from . import search_sequential as ss
from . import search_sequential_sort as sss
from . import search_mblock as smb
from . import search_binary as sbi
from . import search_binary_tree as sbit
from . import search_hash as sh

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
        elif x == "binary_tree":
            return sbit.binary_tree_search(verbose)
        elif x == "hash":
            return sh.hash_search(verbose)
        else:
            print("error:unknown method : ", x)
            exit(-1)
