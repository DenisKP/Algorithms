# Первая версия
print("Введите три разных числа")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if b > a > c or c > a > b:
    print(f"Среднее число из введенных вами {a}")
elif a > c > b or b > c > a:
    print(f"Среднее число из введенных вами {c}")
else:
    print(f"Среднее число из введенных вами {b}")


# вторая версия как мне кажется более правильная
print("Введите три разных числа")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if b > a > c or c > a > b:
    d = a
elif a > c > b or b > c > a:
    d = c
else:
    d = b
print(f"Среднее число из введенных вами {a}")
