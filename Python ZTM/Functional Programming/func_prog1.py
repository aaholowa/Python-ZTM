from functools import reduce
# functions

# map function


def all_caps(item):
    return item.upper()

# zip function


def low_to_high(item):
    return sorted(item)


# filter function manually
def passing_grade(item):
    passing = []
    for i in item:
        if i >= 50:
            passing.append(i)
    return sorted(passing)

# filter function actual


def above_passing(item):
    return item > 50


# reduce function

def accumulation(acc, item):
    return acc + item


# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
print(list(map(all_caps, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
sorted_numbers = low_to_high(my_numbers)
print(list(zip(my_strings, sorted_numbers)))


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
print(list(filter(above_passing, sorted(scores))))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

print(reduce(accumulation, (my_numbers + scores)))
