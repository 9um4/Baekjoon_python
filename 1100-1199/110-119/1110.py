n = input()
result = -1
loop = 0
while result != n:
    if loop == 0:
        result = n
    if len(result) == 1:
        result = str(11*int(result))
        loop += 1
    else:
        result = str((10*(int(result)%10))+((int(result[0])+int(result[1]))%10))
        loop += 1
print(loop)
