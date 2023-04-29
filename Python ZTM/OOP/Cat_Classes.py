# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Mitch', 9)
cat2 = Cat('Wilfred', 20)
cat3 = Cat('Betsy', 27)


# 2 Create a function that finds the oldest cat
def oldest(*kwargs):
    ages = [*kwargs]
    ages.sort()

    return ages[len(ages) - 1]


oldest_age = oldest(cat1.age, cat2.age, cat3.age)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f"The oldest cat is {oldest_age} years old!")
