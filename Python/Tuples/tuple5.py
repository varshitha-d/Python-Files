t = tuple(map(int,input().split(" ")))
c = 0
for i in t:
    if t.count(i)>c:
        c = t.count(i)
        el = i
#max_count = max(t.count(i) for i in t)
#print(max_count)
print(c)
print(el)