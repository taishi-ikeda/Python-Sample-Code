from . import sort_base as sb
from . import sort_merge as sm
from . import sort_bubble as sb
from . import sort_quick as sq
from . import sort_selection as ss
from . import sort_insertion as si
from . import sort_shell as ssh
from . import sort_heap as sh
from . import sort_heap2 as sh2
from enum import Enum

class sort_factory():
    __slots__ = ()

    @classmethod
    def create(cls,x:str,
                   verbose:bool=False,
                   maxsize:int=1000,
                   pivot_selection:str="random") -> sb.sort_base:
        if x == "merge":
            return sm.merge_sort(verbose)
        elif x == "bubble":
            return sb.bubble_sort(verbose)
        elif x == "quick":
            return sq.quick_sort(verbose,pivot_selection)
        elif x == "selection":
            return ss.selection_sort(verbose)
        elif x == "insertion":
            return si.insertion_sort(verbose)
        elif x == "shell":
            return ssh.shell_sort(verbose)
        elif x == "heap":
            return sh.heap_sort(verbose,maxsize)
        elif x == "heap2":
            return sh2.heap_sort2(verbose)
        else:
            print("error:unknown method : ",x)
            exit(-1)
