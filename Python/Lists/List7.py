'''L = list(map(int, input().split(" ")))
l1 = list(map(int, input().split(" ")))
L = L+l1
L.sort()
print(L)'''

L = list(map(int,input().split(" ")))
L.sort(key=len)
L2 = L.sort(reverse=True)
print(L)
print(L2)