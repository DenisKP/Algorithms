import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
count = 0
max_count = 0
max_num = 0
array_copy = array.copy()
while array:
    s = len(array)
    w = array[0]
    for i in range(len(array)):
        if w in array:
            array.remove(w)
            count = s - len(array)
            if count > max_count:
                max_count = count
                max_num = w

print(f"В массиве {array_copy}, \nчисло {max_num} встречается {max_count} раз(а).")
