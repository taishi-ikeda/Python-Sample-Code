from abc import ABCMeta,abstractmethod

class sort_base(metaclass = ABCMeta):
    def __init__(self,verbose:bool)->None:
        self._verbose = verbose
        self._step_counter=0
        pass

    @abstractmethod
    def execute(self)->list[int]:
        pass

    def check_sort(self,li:list[int])->bool:
        for i in range(0,len(li)-1):
            if li[i] > li[i+1]:
                return False
        return True

class merge_sort(sort_base):
    def __init__(self,verbose:bool)->None:
        super().__init__(verbose)

    def merge_array(self,l:list[int],r:list[int])->list[int]:
        if not super().check_sort(l):
            print("input in merge array must be sorted!!")
            return []

        if not super().check_sort(r):
            print("input in merge array must be sorted!!")
            return []

        res=[]
        i,j=0,0
        ll,rl = len(l),len(r)
        while i < ll and j < rl:
            if l[i] < r[j]:
                res.append(l[i])
                i += 1
            else:
                res.append(r[j])
                j += 1
        return res + l[i:] + r[j:]

    def step(self,arr:list[list[int]])->list[list[int]]:
        res = []
        if len(arr)%2==0:
            for i in range(0,len(arr),2):
                a1 = arr[i]
                a2 = arr[i+1]
                res.append(self.merge_array(a1,a2))
        else:
            for i in range(0,len(arr)-1,2):
                a1 = arr[i]
                a2 = arr[i+1]
                res.append(self.merge_array(a1,a2))
            res.append(arr[len(arr)-1])
        return res

    def execute(self,arr:list[int])->list[int]:
        res = [[v] for v in arr]
        while len(res[0]) != len(arr):
            self._step_counter += 1
            if self._verbose:
                print("step_counter : ",self._step_counter,res)
            res = self.step(res)
        return res[0]



