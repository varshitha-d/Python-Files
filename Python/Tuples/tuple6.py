'''l = []
n = int(input())
for i in range(n):
    el = tuple(map(int,input().split(" ")))
    l.append(el)
    if len(el==0):
        del el
print(l)'''

l = [(),(),('',),(1,2),(1,2,3),(5)]
l = [t for t in l if t]
print(l)