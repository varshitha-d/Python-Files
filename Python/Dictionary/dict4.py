#merge two python dictionaries
import operator
d = {}
a = {}
n = int(input())
for i in range(n):
    k,v = map(int,input().split(" "))
    d[k]=v
m = int(input())
for i in range(m):
    k,v = map(int,input().split(" "))
    a[k]=v
c = {}
c = d|a
print(c)


#d2 = d.copy()
#d2.update(a)
#print(d2)