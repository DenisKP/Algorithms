import random

SIZE = 20
MIN_ITEM = - 100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
minus_array = []
min_pos = 0
for i in range(len(array)):
    if array[i] < 0:
        minus_array.append(array[i])
min_digit = minus_array[0]
for i in range(len(minus_array)):
    if minus_array[i] > min_digit:
        min_digit = minus_array[i]
        min_pos = i

print(f"Максимальное отрицательное число в массиве \n{array} \nравно = {min_digit}, находится на позиции {min_pos}")
