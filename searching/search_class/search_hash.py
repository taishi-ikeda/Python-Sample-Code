from . import search_base
import sort.sort_class.sort_factory as sf
import math


class hash_search(search_base.search_base):
    __slots__ = ("_data","_table_size")

    def __init__(self, verbose: bool,
                 table_size:int=100) -> None:
        super().__init__(verbose)
        self._data = [[] for i in range(table_size)]
        self._table_size = table_size

    def get_hash(self,v:int)->int:
        return v % self._table_size

    def search(self,v:int)->bool:
        v_hash = self.get_hash(v)
        for i in range(0,len(self._data[v_hash])):
            if self._data[v_hash][i] == v:
                return True
        return False

    def append(self,v:int):
        v_hash = self.get_hash(v)
        self._data[v_hash].append(v)


    def execute(self, arr: list[int], x: int) -> bool:
        self._data = [[] for i in range(self._table_size)]
        for v in arr:
            self.append(v)

        if self._verbose:
            print(self._data)

        return self.search(x)


