import sort_base
import copy
import numpy as np


class heap_sort(sort_base.sort_base):
    __slots__ = ("_heap", "_maxsize", "_current_size")

    def __init__(self, verbose: bool, maxsize: int) -> None:
        super().__init__(verbose)
        self._maxsize = maxsize
        self._current_size = 0
        self._heap = [0] * self._maxsize

    def push_heap(self, x: int) -> bool:
        if self._current_size >= self._maxsize:
            print("maxsize is not enough!!")
            return False
        self._heap[self._current_size] = x
        self._current_size = self._current_size + 1
        i = self._current_size
        j = int(i * 0.5)
        if self._verbose:
            print("   ", self._heap)
        while j > 0 and x > self._heap[j - 1]:
            self._heap[i - 1] = self._heap[j - 1]
            i = j
            j = int(i * 0.5)
            if self._verbose:
                print("   ", self._heap)
        self._heap[i - 1] = x
        return True

    def delete_max_heap(self) -> [bool, int]:
        if self._current_size == 0:
            print("current heaps size is zero")
            return [False, 0]
        x = self._heap[0]
        self._heap[0] = self._heap[self._current_size - 1]
        self._current_size = self._current_size - 1
        i = 1
        if self._verbose:
            print("   ", self._heap)
        while i * 2 <= self._current_size:
            j = i * 2
            if (
                i * 2 + 1 <= self._current_size
                and self._heap[i * 2 - 1] < self._heap[i * 2]
            ):
                j = i * 2 + 1
            if self._heap[i - 1] >= self._heap[j - 1]:
                break
            else:
                self._heap[j - 1], self._heap[i - 1] = (
                    self._heap[i - 1],
                    self._heap[j - 1],
                )
            i = j
            if self._verbose:
                print("   ", self._heap)
        self._heap[self._current_size] = 0
        return [True, x]

    def execute(self, arr: list[int]) -> list[int]:
        self._heap = [0] * self._maxsize
        self._current_size = 0
        for ele in arr:
            if not self.push_heap(ele):
                return []
            if self._verbose:
                print(self._heap)
        sorted_arr = [0] * len(arr)
        # print(self._heap)
        for i in range(0, len(arr)):
            fl, x = self.delete_max_heap()
            if fl:
                sorted_arr[len(arr) - i - 1] = x
                if self._verbose:
                    print(self._heap)
        return sorted_arr
