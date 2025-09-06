import sort_base
import random


class quick_sort(sort_base.sort_base):
    __slots__ = ()

    def __init__(self, verbose: bool) -> None:
        super().__init__(verbose)

    def execute(self, arr: list[int]) -> list[int]:
        if arr == []:
            return arr
        p = arr[random.randint(0, len(arr) - 1)]
        la = []
        ra = []
        pa = []

        for el in arr:
            if el < p:
                la.append(el)
            elif p < el:
                ra.append(el)
            else:
                pa.append(el)

        return self.execute(la) + pa + self.execute(ra)
