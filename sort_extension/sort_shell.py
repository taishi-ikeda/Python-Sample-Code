import sort_base
import copy

class shell_sort(sort_base.sort_base):
    __slots__=()
    def __init__(self,verbose:bool,\
                 func:sort_base.order_func_base)->None:
        super().__init__(verbose,func)

    def execute(self,arr:list[int])->list[int]:
        arr_copy = copy.copy(arr)
        len_arr_2 = round(len(arr_copy)*0.5)
        gap=len_arr_2
        while gap>0:
            for i in range(gap,len(arr_copy)):
                j=i-gap
                while(j>=0 and \
                        self._func.get(arr_copy[j]) > self._func.get(arr_copy[j+gap])):
                    arr_copy[j],arr_copy[j+gap] = \
                            arr_copy[j+gap],arr_copy[j]
                    j = j-gap
            gap = round(gap*0.5)
        return arr_copy

