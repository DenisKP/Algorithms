# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’]
# и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque


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
    return sum_of_two_str


first_num = deque(input("Введи первое шестнадцатеричное число: "))
second_num = deque(input("Введи второе шестнадцатеричное число: "))
first_num, second_num = reverse_and_len_improve(first_num, second_num)
print(f"Сумма двух введенных шестнадцатеричных чисел: {sum_num(first_num, second_num)}")
