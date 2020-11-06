# https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Lesson2.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1qCV7Yj4lSiz0stoVG1lBsGcx0W9ni_mI%26export%3Ddownload
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
        return f"{(a / b):.2f}"
    elif z == "0":
        return exit(f"Вы выбрали синюю таблетку. ByeBye")
    else:
        return f"Вы выбрали делителем b = 0, а на ноль делить нельзя"


print("Введите два числа и знак +,-,*,/ (второе число не может = '0')")
sign = 1
while sign != 0:
    num_a = input("Введи 1 число ")
    num_b = input("Введи 2 число ")
    while True:
        sign = input("Введи знак, для выхода введи здесь 0 ")
        if sign == '0' or sign == '+' or sign == '-' or sign == '*' or sign == '/':
            break
    print(f"Результат {num_a} {sign} {num_b} = {dfc(num_a, num_b, sign)}")
