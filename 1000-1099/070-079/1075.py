n = int(input())
f = int(input())
ans = 1
if ((n//100)*100)%f == 0:
    print('{0:02}'.format(0))
else:
    ans = (((((n//100)*100)//f)+1)*f)%100
    print('{0:02}'.format(ans))
