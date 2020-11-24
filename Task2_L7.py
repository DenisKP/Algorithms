# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке[0;50).Выведите на экран исходный и отсортированный массивы.
import random
array = [random.uniform(0, 50) for _ in range(10)]


def sort(array_):
    count = len(array_)
    if count > 2:
        array_1 = sort(array_[:count // 2])
        array_2 = sort(array_[count // 2:])
        array_ = array_1 + array_2
        last_ind = len(array_) - 1

        for i in range(last_ind):
            min_val = array_[i]
            min_ind = i

            for j in range(i + 1, last_ind + 1):
                if min_val > array_[j]:
                    min_val = array_[j]
                    min_ind = j

            if min_ind != i:
                array_[i], array_[min_ind] = array_[min_ind], array_[i]

    elif len(array_) > 1 and array_[0] > array_[1]:
        array_[0], array_[1] = array_[1], array_[0]

    return array_


print(f"Исходный массив: \n{array} \nОтсортированный массив: \n{sort(array)}")

