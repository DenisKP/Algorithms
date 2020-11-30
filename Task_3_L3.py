# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

min_int = array[0]
min_pos = 0
max_int = 0
max_pos = 0

for i in range(len(array)):
    if array[i] > max_int:
        max_int = array[i]
        max_pos = i
    elif array[i] <= min_int:
        min_int = array[i]
        min_pos = i

print(f"Максимальное число в массиве - {max_int} \nМинимальное - {min_int}\nСам массив \n{array}")
array[max_pos] = min_int
array[min_pos] = max_int
print(f"Массив с поменянными местами макс и мин - \n{array}")
