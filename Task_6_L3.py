import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
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
sum_el = 0

if min_pos < max_pos:
    for i in range(len(array)):
        if min_pos < i < max_pos:
            sum_el += array[i]
else:
    for i in range(len(array)):
        if max_pos < i < min_pos:
            sum_el += array[i]

print(f"Сумма элементов массива {array}, находящихся между минимальным {min_int} и максимальным {max_int} "
      f"элементами равна {sum_el}")
