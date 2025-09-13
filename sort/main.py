import sort_class.sort_factory as sf
import random

arr = [random.randint(-100, 100) for i in range(20)]
print(arr)
SortMerge = sf.sort_factory.create("merge",False)
arr_merge = SortMerge.execute(arr)
print(arr_merge)

SortBubble = sf.sort_factory.create("bubble",False)
arr_bubble = SortBubble.execute(arr)
print(arr_bubble)

SortQuick = sf.sort_factory.create("quick",False)
arr_quick = SortQuick.execute(arr)
print(arr_quick)

SortSelection = sf.sort_factory.create("selection",False)
arr_selection = SortSelection.execute(arr)
print(arr_selection)

SortInsertion = sf.sort_factory.create("insertion",False)
arr_insertion = SortInsertion.execute(arr)
print(arr_insertion)

SortShell = sf.sort_factory.create("shell",False)
arr_shell = SortShell.execute(arr)
print(arr_shell)

SortHeap = sf.sort_factory.create("heap",False,1000)
arr_heap = SortHeap.execute(arr)
print(arr_heap)

SortHeap2 = sf.sort_factory.create("heap2",False)
arr_heap2 = SortHeap2.execute(arr)
print(arr_heap2)
