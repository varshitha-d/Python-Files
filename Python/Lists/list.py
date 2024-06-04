#creating and printing a list
list = [2, 3, "Dog", True, 9.99]
print(list)

# to print integers in the list
for i in range(len(list)):
    if type(list[i])==int:
        print(list[i])

#append is used to add an elemnt to the list at the end
list.append("cat")
print(list)

#remove is used to add an element from the list
list.remove("Dog")
print(list)