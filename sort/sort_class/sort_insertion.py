from . import sort_base
import copy


class insertion_sort(sort_base.sort_base):
    __slots__ = ()

    def __init__(self, verbose: bool) -> None:
        super().__init__(verbose)

    def execute(self, arr: list[int]) -> list[int]:
        arr_copy = copy.copy(arr)
        for i in range(1, len(arr_copy)):
            x = arr_copy[i]
            j = i
            while j > 0 and arr_copy[j - 1] > x:
                arr_copy[j] = arr_copy[j - 1]
                j = j - 1
            arr_copy[j] = x
            if self._verbose:
                print(arr_copy)
        return arr_copy
