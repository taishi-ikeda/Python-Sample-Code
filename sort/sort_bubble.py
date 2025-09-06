import sort_base
import copy


class bubble_sort(sort_base.sort_base):
    __slots__ = ()

    def __init__(self, verbose: bool) -> None:
        super().__init__(verbose)

    def execute(self, arr: list[int]) -> list[int]:
        arr_copy = copy.copy(arr)
        for i in range(0, len(arr_copy) - 1):
            for j in range(0, len(arr_copy) - i - 1):
                if arr_copy[j] > arr_copy[j + 1]:
                    arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                    if self._verbose:
                        print(arr_copy)
        return arr_copy
