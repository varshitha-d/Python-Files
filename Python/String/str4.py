str = input()
spaces = " "
result = " "
for char in str:
    if char == " ":
        spaces += char
    else:
        result += char
final_string = spaces + result
print(final_string)
