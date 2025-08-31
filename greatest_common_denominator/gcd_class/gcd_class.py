from abc import ABCMeta,abstractmethod

class gcd_base(metaclass = ABCMeta):
    def __init__(self)->None:
        pass
    @abstractmethod
    def get(self,a:int,b:int)->int:
        pass

    def check_parameter(self,a:int,b:int)->bool:
        if a<=0 or b<=0:
            print("a and b must be positive!!")
            return False
        return True


class simple_gcd(gcd_base):
    def __init__(self)->None:
        super().__init__()

    def get(self,a:int,b:int)->int:
        if not super().check_parameter(a,b):
            return 0
        if a < b:
            a,b = b,a
        x=b
        while True:
            if a%x == 0 and b%x==0:
                return x
            x-=1

class euclidean_algo(gcd_base):
    def __init__(self)->None:
        super().__init__()

    def get(self,a:int,b:int)->int:
        if not super().check_parameter(a,b):
            return 0
        if a < b:
            a,b = b,a
        while True:
            r = a%b
            if r==0:
                return b
            a,b = b,r


