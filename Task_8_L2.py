def dig_calc(a, b, d=0):
    while b > 0:
        c = b % 10
        b //= 10
        if c == a:
            d += 1
        return dig_calc(a, b, d)
    return d


print("Введите  какое число будем искать и сколько чисел введете ")
x = int(input("Какое число искать? "))
dig_q = int(input("Сколько чисел введете? "))
sum_x = 0
while dig_q > 0:
    dig = int(input("Введите натуральное число "))
    sum_x += dig_calc(x, dig)
    dig_q -= 1
print(f"Число {x} встречается в веденных Вами числах {sum_x} раз")
