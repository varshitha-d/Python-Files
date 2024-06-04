#find the maximum occuring character in a string
s = input()
max_char = max(s, key=s.count)
print(f"Maximum occuring character: {max_char}")