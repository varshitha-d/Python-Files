#create a string from two given strings concatenating uncommon characters of the 
#said strings
s = input()
s1 = input()
s2 = ""
s3 = s+s1
for i in s3:
    if s3.count(i)==1:
        s2 += i
print(s2)
'''uncommon_chars = "".join(set(s)^set(s1))
print(uncommon_chars)'''