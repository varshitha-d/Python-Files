import operator
d = {}
n = int(input())
for i in range(n):
    k,v = map(int,input().split(" "))
    d[k]=v
k = int(input())
if k in d:
    print("Key is present in the dictionary")
else:
    print("Key is not present in the dictionary")
