a = {1,2,3,4}
b = {2,3,5,6}
print("Union : ",a.union(b))
c=(a.intersection(b))
print("Intersection : ",c)
a.intersection_update(b)
print("Intersection_update : ",a)
a = {1,2,3,4}
b = {2,3,5,6}
d = a.difference(b)
print("Difference : ",d)
a.difference_update(b)
print("Difference_update : ",a)
a = {1,2,3,4}
b = {2,3,5,6}
e = a.symmetric_difference(b)
print("Symmetric_difference : ",e)
a.symmetric_difference_update(b)
print("Symmetric_differnce : ",a)
a = {1,2,3,4}
b = {2,3,5,6}
print("Disjoint : ",a.isdisjoint(b))
print("Subset : ",a.issubset(b))
print("Superset : ",a.issuperset(b))