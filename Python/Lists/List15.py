#to get the sum of the largest number of the list among the other lists within the list.
n = int(input())
L = []
max = 0
index = 0
for i in range(n):
    el = list(map(int,input().split(" ")))
    L.append(el)
    Sum = sum(el[:])
    if Sum > max:
        max = Sum
        index = i
print(i)

'''n = int(input())
a = [map(ingt,input().split()) for i in range(n)]
m = 0
for i in a:
    s = sum(i)
    if s > m:
        m = s
        ind = a.index(i)
print(ind)'''
