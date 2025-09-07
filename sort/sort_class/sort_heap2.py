from . import sort_base
import copy
import numpy as np


class heap_sort2(sort_base.sort_base):
    __slots__ = "_heap"

    def __init__(self, verbose: bool) -> None:
        super().__init__(verbose)

    def execute(self, arr: list[int]) -> list[int]:
        n = len(arr)
        arr_copy = copy.copy(arr)
        if self._verbose:
            print(arr_copy)
        for k in range(int(n / 2), 0, -1):
            i = k
            j = 2 * i
            x = arr_copy[i - 1]
            while j <= n:
                if j < n and arr_copy[j] > arr_copy[j - 1]:
                    j = j + 1
                if x < arr_copy[j - 1]:
                    arr_copy[i - 1] = arr_copy[j - 1]
                    i = j
                    j = 2 * i
                else:
                    break
            arr_copy[i - 1] = x
            if self._verbose:
              print(arr_copy)

        if self._verbose:
          print("finish push heap")
        for k in range(n - 1, 0, -1):
            x = arr_copy[k]
            arr_copy[k] = arr_copy[0]
            i = 1
            j = 2
            while j <= k:
                if j < k and arr_copy[j] > arr_copy[j - 1]:
                    j = j + 1
                if x < arr_copy[j - 1]:
                    arr_copy[i - 1] = arr_copy[j - 1]
                    i = j
                    j = 2 * i
                else:
                    break
            arr_copy[i - 1] = x
            if self._verbose:
              print(arr_copy)
        return arr_copy
