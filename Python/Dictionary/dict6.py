l1 = list(map(int,input().split(" ")))
l2 = list(map(int,input().split(" ")))
#d = {l1[i]:l2[i] for i in range(len(l1)) }
d = dict(zip(l1,l2))
print(d)

'''
Input:
10 5 6
9 2 10
Output:
{10: 9, 5: 2, 6: 10}'''