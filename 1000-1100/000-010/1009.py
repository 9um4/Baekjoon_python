num = int(input())
temp1 = 0
temp2 = 0
temp3 = 0
ans = []
for k in range (0, num):
    temp1, temp2 = input().split(" ")
    temp1 = int(temp1)%10
    temp2 = (int(temp2)%4)+4
    temp3 = (temp1 ** temp2)%10
    if temp3 == 0 :
        temp3 = 10
    print(temp3)
