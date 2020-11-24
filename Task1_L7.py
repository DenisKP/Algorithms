import random

array = [random.randint(-100, 100) for _ in range(5)]
print(f"Массив до сортировки - {array}")
n = 1
check = 0
while n < len(array):
    for i in range(len(array)-n):
        check = array.copy()
        if array[i] < array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
    if array == check:
        print("We finished early then cycle ends, Happy Ending")
        break
    n += 1

print(f"Отсортированный массив - \n{array}")
