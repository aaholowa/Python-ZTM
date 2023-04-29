# square root

list1 = [5, 4, 3]


def root(item):
    empty = []
    for i in item:
        empty.append(i*i)

    return empty


print(root(list1))
print(list(map(lambda item: item * item, list1)))

# list sorting
# sort by the second number in the tuple

list2 = [(0, 2), (4, 3), (9, 9), (10, -1)]

list2.sort(key=lambda item: item[1])
print(list2)
