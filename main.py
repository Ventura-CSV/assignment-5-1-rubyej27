import random


def sumoProduct(l1, l2):
    sum = 0
    m = len(numbers2)
    n = len(numbers1)
    for i in range(0, n):
        for j in range(0, m):
            sumoProduct = i * j
            return sumoProduct


numbers1 = [5, 3, 1, 1, 2]
numbers2 = [1, 2, 2, 9, 5]
result = sumoProduct(numbers1, numbers2)
print('Your result : ', result)


numbers1 = [random.randint(1, 10) for i in range(5)]
numbers2 = [random.randint(1, 10) for i in range(5)]
print('numbers 1 ', numbers1)
print('numbers 2 ', numbers2)
result = sumoProduct(numbers1, numbers2)
print('Your result : ', result)

##
