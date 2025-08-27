import sort_base
import random

class quick_sort(sort_base.sort_base):
    def __init__(self,verbose:bool,
                 func:sort_base.order_func_base)->None:
        super().__init__(verbose,func)

    def execute(self,arr:list[int])->list[int]:
        if arr==[]:
            return arr
        p = arr[random.randint(0,len(arr)-1)]
        la = []
        ra = []
        pa = []

        for el in arr:
            if self._func.get(el) < self._func.get(p):
                la.append(el)
            elif self._func.get(p) < self._func.get(el):
                ra.append(el)
            else:
                pa.append(el)

        return self.execute(la) + \
                pa + \
                self.execute(ra)



