# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
# называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в
# другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
# сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
import random
m = random.randint(1, 100)
s = m   # for test func

array = [random.randint(1, 100) for _ in range(2 * m + 1)]
array_copy = array.copy()

sum_arr = 0
n = 0
while m != -1:
    n = min(array_copy)
    array_copy.remove(n)
    m -= 1
print(f"Для массива \n{array} \nМедианна составляет - {n}")
# Test code by sort
nm = 1
while nm < len(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    nm += 1
print(f'Test check median - {array[s]}')
