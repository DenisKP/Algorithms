import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

a = []
for i in range(len(array)):
    if array[i] % 2 == 0:
        a.append(i)
print(f"В массиве {array}, четные элементы находятся на позициях \n {a}")
