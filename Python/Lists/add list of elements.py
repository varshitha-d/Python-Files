list = [10, 20, 0.5, 10.5, 1.5, 11, 13, 15]
evens=0
odds=0
fl=0
for i in range(len(list)):
    if type(list[i])==int:
        if list[i]%2==0:
            evens+=list[i]
        elif list[i]%2!=0:
            odds+=list[i]
    else:
        fl+=list[i]
print("Sum of even numbers : ",evens)
print("Sum of odd numbers : ",odds)
print("Sum of float numbers : ",fl)  