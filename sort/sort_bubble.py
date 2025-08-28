import sort_base
import copy

class bubble_sort(sort_base.sort_base):
    __slots__=()
    def __init__(self,verbose:bool)->None:
        super().__init__(verbose)

    def execute(self,arr:list[int])->list[int]:
        arr_copy = copy.copy(arr)
        for i in range(0,len(arr_copy)):
            for j in range(i,len(arr_copy)):
                if arr_copy[i] > arr_copy[j]:
                    arr_copy[i],arr_copy[j] = arr_copy[j],arr_copy[i]
        return arr_copy

