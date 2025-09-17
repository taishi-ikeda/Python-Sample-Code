import search_class.search_factory as sf
import random

sample_list = [65,190,-10]

arr = [random.randint(-200, 200) for i in range(100)]
print(arr)
SearchSequential = sf.search_factory.create("sequential", False)
for v in arr:
    SearchSequential.append(v)

for i in sample_list:
    flag = SearchSequential.find(i)
    print("SearchSequential :", flag)

SearchSequentialSort = sf.search_factory.create("sequential_sort", False)
for v in arr:
    SearchSequentialSort.append(v)

for i in sample_list:
    flag = SearchSequentialSort.find(i)
    print("SearchSequentialSort : ", flag)

SearchMBlock = sf.search_factory.create("mblock", False)
for v in arr:
    SearchMBlock.append(v)

for i in sample_list:
    flag = SearchMBlock.find(i)
    print("SearchMBlock : ", flag)

SearchBinary = sf.search_factory.create("binary", False)
for v in arr:
    SearchBinary.append(v)

for i in sample_list:
    flag = SearchBinary.find(i)
    print("SearchBinary : ", flag)

SearchBinaryTree = sf.search_factory.create("binary_tree", False)
for v in arr:
    SearchBinaryTree.append(v)

for i in sample_list:
    flag = SearchBinaryTree.find(arr, i)
    print("SearchBinaryTree : ", flag)

SearchHash = sf.search_factory.create("hash", False)
for v in arr:
    SearchHash.append(v)

for i in sample_list:
    flag = SearchHash.find(i)
    print("SearchHash : ", flag)


