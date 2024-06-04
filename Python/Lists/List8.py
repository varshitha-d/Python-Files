#swap first and last elements
L = input().split(" ")
L[0],L[-1] = L[-1],L[0]
print(L)