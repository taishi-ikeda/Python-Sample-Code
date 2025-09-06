import sort_base
import copy


class shell_sort(sort_base.sort_base):
    __slots__ = ()

    def __init__(self, verbose: bool) -> None:
        super().__init__(verbose)

    def execute(self, arr: list[int]) -> list[int]:
        arr_copy = copy.copy(arr)
        len_arr_2 = round(len(arr_copy) * 0.5)
        gap = len_arr_2
        while gap > 0:
            for i in range(gap, len(arr_copy)):
                temp = arr_copy[i]
                j = i
                while j >= gap and arr_copy[j - gap] > temp:
                    arr_copy[j] = arr_copy[j - gap]
                    j = j - gap
                arr_copy[j] = temp
                if self._verbose:
                    print(arr_copy)
            gap = round(gap * 0.5)
        return arr_copy
