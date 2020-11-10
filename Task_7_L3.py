import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)
min_1 = array[0]
array_copy = array.copy()
for i in range(len(array)):
    if array[i] < min_1:
        min_1 = array[i]
array_copy.remove(min_1)
min_2 = array_copy[0]
for i in range(len(array_copy)):
    if array_copy[i] <= min_2:
        min_2 = array_copy[i]
print(f"Два минимальных числа массива {array} \n= {min_1},{min_2}")
