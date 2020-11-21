# Первый вариант
from collections import deque
import sys


def sum_deq_func(sum_mem_, sum_deq=0):      # функция подсчета для всех вариантов
    for x in sum_mem_:
        sum_deq += sys.getsizeof(x)
        print(f"{x= }, {type(x)= }")  # сделал для проверки себя результат отсюда удалил
        if type(x) == str or type(x) == int:
            continue
        elif type(x) == list or type(x) == deque or type(x) == tuple:
            for n in x:
                sum_deq += sys.getsizeof(n)
        elif type(x) == dict:
            for n in x:
                sum_deq += sys.getsizeof(x)
                sum_deq += sys.getsizeof(x[n])
    return sum_deq


def reverse_and_len_improve(first_n, second_n):
    second_n.reverse()  # разворачиваем деки для удобства
    first_n.reverse()

    while len(first_n) != len(second_n):    # ровняем длину дек
        if len(first_n) > len(second_n):
            second_n.append("0")
        elif len(second_n) > len(first_n):
            first_n.append("0")
    second_n.append("0")    # добавляем нули для того чтобы функция сложения отработала если при сложении первых чисел
    first_n.append("0")     # будет сумма 16+ и придется переносить "единицу"

    return first_n, second_n


def sum_num(first_n, second_n):
    dict_16 = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11,
               "C": 12, "D": 13, "E": 14, "F": 15, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
    dict_16_rev = {value: key for key, value in dict_16.items()}
    # создали словарь и его развернутую копию, для вытаскиваний значений
    sum_list = deque()
    sum_of_two_str = ""
    n = 0

    for i in range(len(first_n)):   # перебор по столбикам плюс сложение значений и переносов
        a = dict_16.get(first_n[i])
        b = dict_16.get(second_n[i])
        c = a + b + n
        n = 0
        while c > 16:
            c -= 16
            n += 1
        c = dict_16_rev.get(c)
        sum_list.insert(0, c)
    if sum_list[0] == "0":  # отбрасывание лишнего первого 0 если он остался
        sum_list.remove("0")
    for i in sum_list:  # делаем красивый вывод результата строкой из деки
        sum_of_two_str += i
    sum_mem.append(sum_list)  # добавляем переменные
    sum_mem.append(n)
    sum_mem.append(dict_16)
    sum_mem.append(dict_16_rev)
    sum_mem.append(sum_of_two_str)
    return sum_of_two_str


sum_mem = deque()
first_num = deque(input("Введи первое шестнадцатеричное число: "))
second_num = deque(input("Введи второе шестнадцатеричное число: "))
sum_mem.append(first_num)
sum_mem.append(second_num)
first_num_rev, second_num_rev = reverse_and_len_improve(first_num, second_num)
sum_mem.append(first_num_rev)
sum_mem.append(second_num_rev)
print(f"Сумма двух введенных шестнадцатеричных чисел: {sum_num(first_num, second_num)}")

print(f"Всего использовано памяти на переменные: {sum_deq_func(sum_mem)}")

# Введи первое шестнадцатеричное число: a2
# Введи второе шестнадцатеричное число: c4f
# Сумма двух введенных шестнадцатеричных чисел: cf1
# Всего использовано памяти на переменные: 43486

# Второй вариант, честно подсмотренный у вас, взял его как вариант, потому что в итоге есть использование двух словарей,
# при этом словари меньше,и созданы заранее, а не копированы в коде, как у меня, плюс само использование меньшего кол-ва
# переменных


dict_16_rev = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               'A', 'B', 'C', 'D', 'E', 'F')

dict_16 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
           'C': 12, 'D': 13, 'E': 14, 'F': 15}


def sum_num_2(first, second):

    first = first.copy()
    second = second.copy()

    if len(second) > len(first):
        first, second = second, first

    second.extendleft("0" * (len(first) - len(second)))

    result = deque()
    transferal = 0
    while len(first) != 0:
        first_num = dict_16[first.pop()]
        second_num = dict_16[second.pop()]

        result_num = first_num + second_num + transferal

        if result_num >= len(dict_16_rev):
            transferal = 1
            result_num -= len(dict_16_rev)
        else:
            transferal = 0

        result.appendleft(dict_16_rev[result_num])

    if transferal == 1:
        result.appendleft("1")  # усвоил, что максимальное значение будет 1, и не надо писать что то длиннее
    sum_mem.append(first)
    sum_mem.append(second)
    sum_mem.append(result)
    sum_mem.append(transferal)
    return result


first_nu = deque(input("Введи первое шестнадцатеричное число: ").upper())
second_nu = deque(input("Введи второе шестнадцатеричное число: ").upper())
sum_mem = deque()
print(f"Сумма двух введенных шестнадцатеричных чисел: {list(sum_num_2(first_nu, second_nu))}")

sum_mem.append(dict_16)
sum_mem.append(dict_16_rev)
sum_mem.append(first_nu)
sum_mem.append(second_nu)
print(f"Всего использовано памяти на переменные: {sum_deq_func(sum_mem)}")
# Введи первое шестнадцатеричное число: a2
# Введи второе шестнадцатеричное число: c4f
# Сумма двух введенных шестнадцатеричных чисел: ['C', 'F', '1']
# Всего использовано памяти на переменные: 15836
#
# Третий вариант. Запрещенный на прошлом уроке, но не запрещенный на этом.
#
first_nu = input("Введи первое шестнадцатеричное число: ")
second_nu = input("Введи второе шестнадцатеричное число: ")
sum_16 = hex(int(first_nu, 16) + int(second_nu, 16))
print(f"Сумма двух введенных шестнадцатеричных чисел: {sum_16}")
sum_mem = deque()
sum_mem.append(first_nu)
sum_mem.append(second_nu)
sum_mem.append(sum_16)

print(f"Всего использовано памяти на переменные: {sum_deq_func(sum_mem)}")
# Введи первое шестнадцатеричное число: a2
# Введи второе шестнадцатеричное число: c4f
# Сумма двух введенных шестнадцатеричных чисел: 0xcf1
# Всего использовано памяти на переменные: 157
# Вывод:
# Рассмотрены три варианта решения задачи:
#    Самый оптимальный вариант, естественно использующий встроенные функции написанные на языке С. При использовании hex
# Затрачено памяти 157 байт на все три переменные, что лучше всего. Так как str значения не надо преобразовывать в
# лист или кортеж. Плюс для дальнейшего вывод и вычислений не нужно создавать новые переменные.
# Мой первично сданный способ затрачивает наибольшее кол-во памяти 5092 байта, из-за создания огромного кол-ва
# переменных.
# Интерпретатор Python 3.8, Windows 10 X64
