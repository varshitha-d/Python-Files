'''def sub(*integers):#unpacking of a lsit
    result = 0
    for x in integers:
        result -= x
    return result
integers = list(map(int,input().split(" ")))
print(sub(integers))'''

def concatenate(**words):#realpython
    result = ''
    for arg in words.values():
        result += arg
    return result
print(concatenate(a = 'Real ', b='Python ', c='Is ', d="Great ", e="!"))