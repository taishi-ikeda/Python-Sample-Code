from . import sort_base
import random


class quick_sort(sort_base.sort_base):
    __slots__ = ("_pivot_selection")

    def __init__(self, verbose: bool, pivot_selection: str) -> None:
        super().__init__(verbose)
        self._pivot_selection = pivot_selection

    def execute(self, arr: list[int]) -> list[int]:
        if arr == []:
            return arr
        if self._pivot_selection == "head":
            p = arr[0]
        elif self._pivot_selection == "end":
            p = arr[-1]
        elif self._pivot_selection == "center":
            p = arr[int(len(arr) * 0.5)]
        elif self._pivot_selection == "rough_mid":
            ph = arr[0]
            pe = arr[-1]
            pc = arr[int(len(arr) * 0.5)]
            if ph < pe:
                if pc < ph:
                    p = ph
                else:
                    if pe < pc:
                        p = pe
                    else:
                        p = pc
            else:
                if ph < pc:
                    p = ph
                else:
                    if pe < pc:
                        p = pc
                    else:
                        p = pe
        elif self._pivot_selection == "random":
            p = arr[random.randint(0, len(arr) - 1)]
        else:
            print("uknown pivot_selection:", self._pivot_selection)
            exit(0)

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

        if self._verbose:
            print("(la|pa|ra) = ", la, "|", pa, "|", ra)
        return self.execute(la) + pa + self.execute(ra)
