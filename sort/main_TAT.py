import sort_merge as sm
import sort_bubble as sb
import sort_quick as sp
import sort_selection as ss
import sort_insertion as si
import sort_shell as ssh
import sort_heap as sh
import time
import random
import matplotlib.pyplot as plt
import numpy as np

sample_num = 2000
average_run = 10

x_list = []
y_list_bubble = []
y_list_insertion = []
y_list_selection=[]
y_list_quick=[]
y_list_merge=[]
y_list_heap=[]
y_list_shell=[]

SortMerge = sm.merge_sort(False)
SortBubble = sb.bubble_sort(False)
SortQuick = sp.quick_sort(False)
SortSelection = ss.selection_sort(False)
SortInsertion = si.insertion_sort(False)
SortShell = ssh.shell_sort(False)
SortHeap = sh.heap_sort(False,100000)

for l in range(10,2000,10):
    TAT_bubble=0.0
    TAT_insertion=0.0
    TAT_selection=0.0
    TAT_quick=0.0
    TAT_merge=0.0
    TAT_heap=0.0
    TAT_shell=0.0

    for i_run in range(0,average_run):
        arr=[]
        for j in range(0,l):
            arr.append(random.randint(-l,l))

        start_time=time.time()
        arr_merge=SortMerge.execute(arr)
        end_time=time.time()
        TAT_merge = TAT_merge + end_time - start_time

        start_time=time.time()
        arr_bubble = SortBubble.execute(arr)
        end_time=time.time()
        TAT_bubble = TAT_bubble + end_time - start_time

        start_time=time.time()
        arr_quick = SortQuick.execute(arr)
        end_time=time.time()
        TAT_quick = TAT_quick + end_time - start_time

        start_time=time.time()
        arr_selection = SortSelection.execute(arr)
        end_time=time.time()
        TAT_selection = TAT_selection + end_time - start_time

        start_time=time.time()
        arr_insertion = SortInsertion.execute(arr)
        end_time=time.time()
        TAT_insertion = TAT_insertion + end_time - start_time

        start_time=time.time()
        arr_shell = SortShell.execute(arr)
        end_time=time.time()
        TAT_shell = TAT_shell + end_time - start_time

        start_time=time.time()
        arr_heap = SortHeap.execute(arr)
        end_time=time.time()
        TAT_heap = TAT_heap + end_time - start_time

    y_list_bubble.append(TAT_bubble/average_run)
    y_list_insertion.append(TAT_insertion/average_run)
    y_list_selection.append(TAT_selection/average_run)
    y_list_quick.append(TAT_quick/average_run)
    y_list_merge.append(TAT_merge/average_run)
    y_list_heap.append(TAT_heap/average_run)
    y_list_shell.append(TAT_shell/average_run)
    x_list.append(l)


plt.xlabel("size array")
plt.ylabel("TAT sec")
plt.plot(x_list,y_list_bubble,label="bubble",marker='o',linestyle='none')
plt.plot(x_list,y_list_insertion,label="insertion",marker='o',linestyle='none')
plt.plot(x_list,y_list_selection,label="selection",marker='o',linestyle='none')
plt.plot(x_list,y_list_quick,label="quick",marker='o',linestyle='none')
plt.plot(x_list,y_list_merge,label="merge",marker='o',linestyle='none')
plt.plot(x_list,y_list_heap,label="heap",marker='o',linestyle='none')
plt.plot(x_list,y_list_shell,label="shell",marker='o',linestyle='none')

plt.legend()
plt.savefig("time_measure.png")
