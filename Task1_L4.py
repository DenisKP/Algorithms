import timeit
import cProfile
import random
# Первый вариант

SIZE = 10000000
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array_copy = array.copy()
s1 = """
count = 0
max_count = 0
max_num = 0
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
"""
# print(f"В массиве {array_copy}, \nчисло {max_num} встречается {max_count} раз(а).")
# Для массива 100
print(timeit.timeit("s1", number=100, globals=globals()))   # 5.199999999996874e-06
print(timeit.timeit("s1", number=100, globals=globals()))   # 4.7000000000102515e-06
print(timeit.timeit("s1", number=100, globals=globals()))   # 4.599999999993498e-06
cProfile.run("s1")
# 3 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# Для массива 500
# 6.0000000000060005e-06
# 3.899999999987247e-06
# 3.7999999999982492e-06
# 3 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# Для массива 1000
# 5.0000000000050004e-06
# 4.599999999993498e-06
# 4.400000000001625e-06
# 3 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}

# Второй вариант
#
#
# def array_cr(size, min_item=-100, max_item=100):
#     array_f = [random.randint(min_item, max_item) for _ in range(size)]
#     return array_f
#
#
# def try_new(ar, max_count=0, max_num=0):
#     ar_c = ar.copy()
#     while ar_c:
#         s = len(ar_c)
#         w = ar_c[0]
#         for i in range(len(ar_c)):
#             if w in ar_c:
#                 ar_c.remove(w)
#                 count = s - len(ar_c)
#                 if count > max_count:
#                     max_count = count
#                     max_num = w
#
#     return max_num, max_count
#
#
# siz = 100
# array = array_cr(siz)
# m_n, m_c = (try_new(array))
# print(array, m_n, m_c)

# Для Массива длиной 100
print(timeit.timeit("try_new(array)", number=100, globals=globals()))  # 0.6600731999999999
print(timeit.timeit("try_new(array)", number=100, globals=globals()))  # 0.6570994
print(timeit.timeit("try_new(array)", number=100, globals=globals()))  # 0.6563641000000002
cProfile.run("try_new(array)")
# 371 function calls in 0.004 seconds
#
#     Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#         1    0.004    0.004    0.004    0.004 Task1_L4.py:11(try_new)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#       266    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       100    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}

# Для Массива длиной 500
# 32.029049900000004
# 32.477236
# 32.2581737
# 1359 function calls in 0.337 seconds
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.337    0.337 <string>:1(<module>)
#        1    0.335    0.335    0.337    0.337 Task1_L4.py:63(try_new)
#        1    0.000    0.000    0.337    0.337 {built-in method builtins.exec}
#      854    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        1    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      500    0.001    0.000    0.001    0.000 {method 'remove' of 'list' objects}

# Для Массива длиной 1000
# 151.1757008
# 156.0373474
# 152.81888790000005
# 2403 function calls in 1.498 seconds

#  Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    1.498    1.498 <string>:1(<module>)
#        1    1.492    1.492    1.498    1.498 Task1_L4.py:63(try_new)
#        1    0.000    0.000    1.498    1.498 {built-in method builtins.exec}
#     1398    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        1    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     1000    0.006    0.000    0.006    0.000 {method 'remove' of 'list' objects}

# Третий вариант
s2 = """
num = array[0]
max_count = 1
for i in range(len(array)):
    times = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            times += 1
    if times > max_count:
        max_count = times
        num = array[i]
f"""
# print(f' {num} встречется {max_count} раз')
# Для массива 100
print(timeit.timeit("s2", number=100, globals=globals()))   # 5.000000000005e-07
print(timeit.timeit("s2", number=100, globals=globals()))   # 6.999999999993123e-07
print(timeit.timeit("s2", number=100, globals=globals()))   # 2.3999999999996247e-06
cProfile.run("s2")
# 3 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Для массива 500
# 5.999999999964367e-07
# 7.000000000062512e-07
# 2.5000000000025002e-06
# 3 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}

# Для массива 1000

# 6.999999999993123e-07
# 6.999999999993123e-07
# 2.9000000000001247e-06
# 3 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}

# # Выводы
# Протестировав 3 варианта кода. Понятно что копирование массива удаление из него элементов по перебору сразу дает O(n)
# в квадрате. А когда к такому методу добавляется рекурсия(вариант2), то на массив длиной 1000 у компа с 12 ядрами 3300
# и 32 гигами оперативы уходит 156 секунд, а ноутбук висиь вплоть до 5-6 минут. Хотя первый метод и оказался быстрым,
# все равно при величине массива например 10_000_000 код выполняется дольше чем в третьем варианте, а во втором вообще
# вешает пичарм.
# Отсюда вывод, что даже через 3.5 вложенных цикла код работает намного быстрее.
# Победитель метод - 3
