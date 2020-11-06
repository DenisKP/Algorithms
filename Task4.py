import random

print("Выберите тип вводимого диапазона 1 - целые числа, 2 - вещественные числа, 3 - буквы английского алфавита")
s = int(input("Ваш выбор "))
a = input("a = ")
b = input("b = ")
if s == 1:
    a = int(a)
    b = int(b)
    r = random.randint(a, b)
    print(f'В диапазоне между {a = } и {b = } случайно выбрали {r}')
else:
    if s == 2:
        a = float(a)
        b = float(b)
        r = random.uniform(a, b)
        print(f'В диапазоне между {a = } и {b = } случайно выбрали {r:.1f}')
    else:
        a = ord(a)
        b = ord(b)
        r = chr(random.randint(a, b))
        print(f'В диапазоне между буквами {chr(a)} и {chr(b)} случайно выбрали {r}')
