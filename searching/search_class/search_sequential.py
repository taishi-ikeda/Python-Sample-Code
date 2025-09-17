from . import search_base


class sequential_search(search_base.search_base):
    __slots__ = ("_data")

    def __init__(self, verbose: bool) -> None:
        super().__init__(verbose)
        self._data = []

    def append(self,x:int):
        self._data.append(x)

    def find(self,x: int) -> bool:
        for i in range(len(self._data)):
            if self._data[i] == x:
                return True
        return False
