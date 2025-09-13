import search_class.search_factory as sf
import random

arr = [random.randint(-200, 200) for i in range(100)]
print(arr)
SearchSequential = sf.search_factory.create("sequential", False)
flag = SearchSequential.execute(arr, 65)
print("SearchSequential :", flag)
flag = SearchSequential.execute(arr, -100)
print("SearchSequential :", flag)

SearchSequentialSort = sf.search_factory.create("sequential_sort", False)
flag = SearchSequentialSort.execute(arr, 65)
print("SearchSequentialSort : ", flag)
flag = SearchSequentialSort.execute(arr, -100)
print("SearchSequentialSort : ", flag)

SearchMBlock = sf.search_factory.create("mblock", False)
flag = SearchMBlock.execute(arr, 65)
print("SearchMBlock : ", flag)
flag = SearchMBlock.execute(arr, -100)
print("SearchMBlock : ", flag)
