import sort_class.sort_factory as sf
import random

arr = [5, 4, 8, 1, 3, 2, 7, 6]

print(arr)
print("bubble sort")
SortBubble = sf.sort_factory.create("bubble",True)
arr_bubble = SortBubble.execute(arr)
print(arr_bubble)

print("selection sort")
SortSelection = sf.sort_factory.create("selection",True)
arr_selection = SortSelection.execute(arr)
print(arr_selection)

print("insertion sort")
SortInsertion = sf.sort_factory.create("insertion",True)
arr_insertion = SortInsertion.execute(arr)
print(arr_insertion)

print("shell sort")
SortShell = sf.sort_factory.create("shell",True)
arr_shell = SortShell.execute(arr)
print(arr_shell)

print("heap sort")
SortHeap = sf.sort_factory.create("heap",True, 10)
arr_heap = SortHeap.execute(arr)
print(arr_heap)

print("heap sort2")
SortHeap2 = sf.sort_factory.create("heap2",True)
arr_heap2 = SortHeap2.execute(arr)
print(arr_heap2)

print("quick sort")
SortQuick = sf.sort_factory.create("quick",True,pivot_selection="head")
arr_quick = SortQuick.execute(arr)
print(arr_quick)

print("merge sort")
SortMerge = sf.sort_factory.create("merge",True)
arr_merge = SortMerge.execute(arr)
print(arr_merge)



