#print length of string without length operators
def len1(str1):
    count = 0
    for char in str1:
        count+=1
    return count
str1 = input()
print(len1(str1))