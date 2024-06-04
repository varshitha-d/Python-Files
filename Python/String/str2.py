#takes input and prints output in upper and lower cases
str = input()
print("Your input in upper case",str.upper())
print("Your input in upper case",str.lower())
str1 = "My car is BmW"
str2 = "BmW"
str3 = str1.replace(str2,str2.upper())
print(str3)