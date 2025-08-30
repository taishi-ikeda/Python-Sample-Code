import gcd_class.gcd_class as gcd


a = 12
b = 232

gcd_method1 = gcd.simple_gcd()
n1 = gcd_method1.get(a,b)
gcd_method2 = gcd.euclidean_algo()
n2 = gcd_method2.get(a,b)
print("(n1,n2)=",(n1,n2))
