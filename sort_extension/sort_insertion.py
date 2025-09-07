import sort_base
import copy


class insertion_sort(sort_base.sort_base):
    __slots__ = ()

    def __init__(self, verbose: bool, func: sort_base.order_func_base) -> None:
        super().__init__(verbose, func)

    def execute(self, arr: list[int]) -> list[int]:
        arr_copy = copy.copy(arr)
        for i in range(0, len(arr_copy)):
            x = arr_copy[i]
            j = i
            while j > 0 and self._func.get(arr_copy[j - 1]) > self._func.get(x):
                arr_copy[j] = arr_copy[j - 1]
                j = j - 1
            arr_copy[j] = x
            if self._verbose:
                print(arr_copy)
        return arr_copy
