import math as m

a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

if c == b:
    print(-1)
elif c < b:
    print(-1)
else:
    print(((-a)//(b-c))+1)
