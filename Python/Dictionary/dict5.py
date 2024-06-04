#remove a key from a dictionary
d = {}
n = int(input())
for i in range(n):
    k,v = map(int,input().split(" "))
    d[k]=v
a = int(input())
d.pop(a)
#if a in d:
#   del d[a]
print(d)

'''Intput:
4
1 2
3 4
5 6
7 8
1
Output:
{3: 4, 5: 6, 7: 8}'''