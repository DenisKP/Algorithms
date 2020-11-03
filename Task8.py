print("Введите год")
a = int(input(" = "))
b = abs(a) % 100

if b != 0:
    c = a % 4
else:
    c = a % 400
if c == 0:
    print(f"Введенный вами год {a} високосный")
else:
    print(f"Введенный вами год {a} не високосный")
