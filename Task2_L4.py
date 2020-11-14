# # По методу эратосфена
num_i = int(input(f"Для нахождения i-го по счёту простого числа, введите i "))
# вижу проблему числа n вдруг пользователь захочет получить число в интервале большем чем 10 000, но тогда n можно
# задавать от num_i хотя мы говорили, что по дефолту не трогаем функцию создания учебного массива для тестов.
n = num_i * 50
array = [i for i in range(n)]
array[1] = 0

for i in range(2, n):
    if array[i] != 0:
        j = i + i
        while j < n:
            array[j] = 0
            j += i

for i in range(len(array)):  # Первый способ - убиваем 0 методом перебора.
    if 0 in array:
        array.remove(0)

for i in array:  # второй способ перебираем весь верхний список при отличии от 0 минусуем 1 пока не дойдем до нуля.
    if i != 0:
        num_i -= 1
        if num_i == 0:
            print(f" Первый способ {i}")


print(f" Второй способ {sieve[num_i-1]}")


# Второй вариант через



# print(num_usual(num_i))
def sieve_f2(k, size):
    array_1 = [2]
    for i in range(3, size):
        for j in array_1:
            if i % j == 0:
                break
            elif i % j != 0 and j != array_1[-1]:
                continue
            else:
                array_1.append(i)
    return array_1[k-1]


num_i = int(input(f"Для нахождения i-го по счёту простого числа, введите i "))
array_size = num_i * 50
print(sieve_f2(num_i, array_size))
