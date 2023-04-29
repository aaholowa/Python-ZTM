list1 = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

dup = set(item for item in list1 if list1.count(item) > 1)
print(dup)
