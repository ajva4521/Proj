#!/usr/bin/env python3
from mymath.advanced import add, sub, mul, div, pow, modulo
from mymath.factorial import factorial
from mymath.fibonacci import fibonacci
a=input("Zadej čislo a:")
a = int(a)
b=0
c=3
d=1

n=6

result = add(a,b,c,d)
print("add({},{},{},{})->{}".format(a,b,c,d,result))

result = div(b,a,c,a)
print("div({},{},{},{})->{}".format(b,a,c,a,result))


result = sub(a,b,c,d)
print("sub({},{},{},{})->{}".format(a,b,c,d,result))

result = mul(a,b,c,d)
print("mul({},{},{},{})->{}".format(a,b,c,d,result))

result = div(a,b,c,d)
print("div({},{},{},{})->{}".format(a,b,c,d,result))

result = pow(a,b,c,d)
print("pow({},{},{},{})->{}".format(a,b,c,d,result))

resut = modulo(a,b)
print("modulo({},{})->{}".format(a,b,result))

r = factorial(a)
print(r)


print("mňau")

result = fibonacci(n)
print(result)
