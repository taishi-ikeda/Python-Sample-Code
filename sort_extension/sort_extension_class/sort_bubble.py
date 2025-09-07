from . import sort_base
import copy


class merge_bubble(sort_base.sort_base):
    __slots__ = ()

    def __init__(self, verbose: bool, func: sort_base.order_func_base) -> None:
        super().__init__(verbose, func)

    def execute(self, arr: list[int]) -> list[int]:
        arr_copy = copy.copy(arr)
        for i in range(0, len(arr_copy)):
            for j in range(i, len(arr_copy)):
                if self._func.get(arr_copy[i]) > self._func.get(arr_copy[j]):
                    arr_copy[i], arr_copy[j] = arr_copy[j], arr_copy[i]
                    if self._verbose:
                        print(arr_copy)
        return arr_copy
