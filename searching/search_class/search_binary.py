from . import search_base
import sort.sort_class.sort_factory as sf
import math


class binary_search(search_base.search_base):
    __slots__ = "_sort"

    def __init__(self, verbose: bool, sort_method: str = "quick") -> None:
        super().__init__(verbose)
        self._sort = sf.sort_factory.create(sort_method)

    def execute(self, arr: list[int], x: int) -> bool:
        size = len(arr)
        sorted_arr = self._sort.execute(arr)

        if self._verbose:
            print(sorted_arr)

        left = 0
        right = size-1

        if x < sorted_arr[0] or sorted_arr[-1] < x:
            return False

        while left < right:
            mid = (right + left)//2
            if self._verbose:
                print("left,mid,right = ",left,mid,right)
            if x < sorted_arr[mid]:
                right = mid
            else:
                left = mid+1
        return sorted_arr[left-1] == x


