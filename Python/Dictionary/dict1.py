import operator
d = {}
n = int(input())
for i in range(n):
    k,v = map(int,input().split(" "))
    d[k]=v
k,v = map(int,input().split(" "))
d[k] = v
#d.update({k:v})
print(d)