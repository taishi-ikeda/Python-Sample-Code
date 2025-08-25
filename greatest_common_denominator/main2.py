import gcd_class as gcd
import time

a_max=1000
b_max=1000

a_list=[a for a in range(1,a_max)]
b_list=[b for b in range(1,b_max)]

print("Simple Start")
gcd_list1=[]
gcd_method1 = gcd.simple_gcd()
start = time.time()
for a in a_list:
    for b in b_list:
        ret = gcd_method1.get(a,b)
        gcd_list1.append(ret)
end = time.time()
time_simple = end - start
print("time simple = ",time_simple)

print("Euclidean Start")
gcd_list2=[]
gcd_method2 = gcd.euclidean_algo()
start = time.time()
for a in a_list:
    for b in b_list:
        ret = gcd_method2.get(a,b)
        gcd_list2.append(ret)
end = time.time()
time_eculidean = end - start
print("time eculidean = ",time_eculidean)
