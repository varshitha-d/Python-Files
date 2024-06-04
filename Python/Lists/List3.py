L = [1,2,3,4,5]
for i in range(1, 4):
    L[i-2] = L[i]
for i in range(0, 4):
    print(L[i], end = " ")