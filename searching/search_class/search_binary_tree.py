from __future__ import annotations
from . import search_base
import sort.sort_class.sort_factory as sf
import math
from typing import Tuple

class node:
    __slots__=("_value",
               "_right",
               "_left")
    def __init__(self,value:int):
        self._value = value
        self._left = None
        self._right = None

    @property
    def value(self)->int:
        return self._value

    @property
    def right(self)->node:
        return self._right

    @property
    def left(self)->node:
        return self._left

    @value.setter
    def value(self,value:int):
        self._value = value

    @right.setter
    def right(self,right:node):
        if isinstance(right,node):
            self._right = right
            return
        else:
            print("error : invalid type")
            exit(-1)

    @left.setter
    def left(self,left:node):
        if isinstance(left,node):
            self._left = left
            return
        else:
            print("error : invalid type")
            exit(-1)

    def __str__(self):
        l = f'{self._left.value}' if self.left else '[]'
        r = f'{self._right.value}' if self.right else '[]'
        return f'{l} <- {self._value} -> {r}'

class binary_search_tree:
    __slots__ = ("_nodes")

    def __init__(self):
        self._nodes = []

    def add_node(self,value)->None:
        node_tmp = node(value)
        if self._nodes:
            p,direction = self.get_parent(value)
            if direction == "":
                return
            if direction == "left":
                p.left = node_tmp
            else:
                p.right = node_tmp
        self._nodes.append(node_tmp)

    def get_parent(self,value)->Tuple[node,str]:
        node = self._nodes[0]
        while node:
            p = node
            if p.value == value:
                return [None,""]
            if value < p.value:
                direction = "left"
                node = p.left
            else:
                direction = "right"
                node = p.right
        return [p,direction]

    def has_value(self,value)->bool:
        p,direction = self.get_parent(value)
        if direction == "":
            return True
        return False

    def __str__(self):
        return str([str(self._nodes[i]) for i in range(0,len(self._nodes))])

class binary_tree_search(search_base.search_base):
    __slots__ = ("_btree")

    def __init__(self, verbose: bool) -> None:
        super().__init__(verbose)
        self._btree = binary_search_tree()

    def append(self,x:int) -> None:
        self._btree.add_node(x)
        if self._verbose:
           print(str(self._btree))

    def find(self, arr: list[int], x: int) -> bool:
        if self._verbose:
            print(str(self._btree))

        return self._btree.has_value(x)


