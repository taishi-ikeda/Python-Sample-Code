import gcd_class.gcd_class as gcd
import time
import random
import matplotlib.pyplot as plt
import numpy as np

sample_num = 2000

max_num=10000000

x_list = []
y_list_simple = []
y_list_euclid = []
gcd_method1 = gcd.simple_gcd()
gcd_method2 = gcd.euclidean_algo()

for num in range(0,sample_num):
    a = random.randint(1,max_num)
    b = random.randint(1,max_num)
    x_list.append(min(a,b))
    start = time.time()
    ns=gcd_method1.get(a,b)
    end = time.time()
    y_list_simple.append(end-start)
    start = time.time()
    ne=gcd_method2.get(a,b)
    end = time.time()
    y_list_euclid.append(end-start)
    if not ns == ne:
        print("Two methods have different results!!")

plt.xlabel("min(a,b)")
plt.ylabel("TAT sec")
plt.plot(x_list,y_list_simple,label="simple",marker='o',linestyle='none')
plt.plot(x_list,y_list_euclid,label="euclid",marker='o',linestyle='none')
plt.legend()
plt.savefig("time_measure.png")
