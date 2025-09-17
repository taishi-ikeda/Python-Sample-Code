import search_class.search_factory as sf
import random

sample_list = [65,210]

arr = [random.randint(-200, 200) for i in range(100)]
print(arr)
SearchSequential = sf.search_factory.create("sequential", False)
for i in sample_list:
    flag = SearchSequential.execute(arr, i)
    print("SearchSequential :", flag)

SearchSequentialSort = sf.search_factory.create("sequential_sort", False)
for i in sample_list:
    flag = SearchSequentialSort.execute(arr, i)
    print("SearchSequentialSort : ", flag)

SearchMBlock = sf.search_factory.create("mblock", False)
for i in sample_list:
    flag = SearchMBlock.execute(arr, i)
    print("SearchMBlock : ", flag)

SearchBinary = sf.search_factory.create("binary", False)
for i in sample_list:
    flag = SearchBinary.execute(arr, i)
    print("SearchBinary : ", flag)

SearchBinaryTree = sf.search_factory.create("binary_tree", False)
for i in sample_list:
    flag = SearchBinaryTree.execute(arr, i)
    print("SearchBinaryTree : ", flag)

SearchHash = sf.search_factory.create("hash", True)
for i in sample_list:
    flag = SearchHash.execute(arr, i)
    print("SearchHash : ", flag)


