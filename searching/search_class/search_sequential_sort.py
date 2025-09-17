from . import search_base
import sort.sort_class.sort_factory as sf


class sequential_sort_search(search_base.search_base):
    __slots__ = ("_sort",
                 "_data")

    def __init__(self, verbose: bool, sort_method: str = "quick") -> None:
        super().__init__(verbose)
        self._sort = sf.sort_factory.create(sort_method)
        self._data = []

    def append(self,x:int):
        self._data.append(x)

    def find(self, x: int) -> bool:
        sorted_arr = self._sort.execute(self._data)

        for i in range(len(sorted_arr)):
            if sorted_arr[i] >= x:
                break
        if sorted_arr[i] == x:
            return True
        return False
