import search_class.search_factory as sf
import random

sample_list = [0,2,4]
arr = [6,9,-1,-4,7,10,0]


SearchBinaryTree = sf.search_factory.create("binary_tree", True)
for v in arr:
    SearchBinaryTree.append(v)

for i in sample_list:
    flag = SearchBinaryTree.find(arr, i)
    print("SearchBinaryTree : ", flag)

arr = [-4,-1,0,6,7,9,10]


SearchBinaryTree = sf.search_factory.create("binary_tree", True)
for v in arr:
    SearchBinaryTree.append(v)

for i in sample_list:
    flag = SearchBinaryTree.find(arr, i)
    print("SearchBinaryTree : ", flag)


