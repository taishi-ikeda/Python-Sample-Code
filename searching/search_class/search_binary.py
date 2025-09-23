from . import search_base
import sort.sort_class.sort_factory as sf
import math


class binary_search(search_base.search_base):
    __slots__ = ("_sort","_data")

    def __init__(self, verbose: bool, sort_method: str = "quick") -> None:
        super().__init__(verbose)
        self._sort = sf.sort_factory.create(sort_method)
        self._data = []

    def append(self,x:int):
        self._data.append(x)

    def find(self,x:int)->None:
        size = len(self._data)
        sorted_arr = self._sort.execute(self._data)

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

            if x == sorted_arr[mid]:
                return True
            elif x < sorted_arr[mid]:
                right = mid-1
            else:
                left = mid+1
        if self._verbose:
           print("left,mid,right = ",left,mid,right)
        return sorted_arr[left] == x


