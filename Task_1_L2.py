# https://drive.google.com/file/d/1qCV7Yj4lSiz0stoVG1lBsGcx0W9ni_mI/view?usp=sharing
def dfc(a, b, z):
    a = float(a)
    b = float(b)
    if z == "+":
        return f"{a + b}"
    elif z == "-":
        return f"{a - b}"
    elif z == "*":
        return f"{a * b}"
    elif z == "/" and b != 0:
        return f"{a / b:.2f}"
    elif z == "0":
        exit(f"Вы выбрали синюю таблетку")
    else:
        return f"Вы выбрали делителем b = 0, а на ноль делить нельзя"


print("Введите два числа и знак +,-,*,/ (второе число не может = '0')")
while True:
    num_a = input("Введи первое натуральное число ")
    num_b = input("Введи второе натуральное число ")
    while True:
        sign = input("Введи знак, для выхода введи здесь 0 ")
        if sign == '0' or sign == '+' or sign == '-' or sign == '*' or sign == '/':
            break
    print(f"Результат {num_a} {sign} {num_b} = {dfc(num_a, num_b, sign)}")
