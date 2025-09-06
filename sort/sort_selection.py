import sort_base
import copy
import sys


class selection_sort(sort_base.sort_base):
    _slots_ = ()

    def __init__(self, verbose: bool) -> None:
        super().__init__(verbose)

    def execute(self, arr: list[int]) -> list[int]:
        arr_copy = copy.copy(arr)
        for i in range(0, len(arr_copy)):
            v_max = -sys.maxsize
            j_max = -1
            for j in range(0, len(arr_copy) - i):
                if v_max < arr_copy[j]:
                    v_max = arr_copy[j]
                    j_max = j
            if self._verbose:
                print(arr_copy)
            arr_copy[len(arr_copy) - i - 1], arr_copy[j_max] = (
                arr_copy[j_max],
                arr_copy[len(arr_copy) - i - 1],
            )
        return arr_copy
