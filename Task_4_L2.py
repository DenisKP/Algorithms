def row_num(a, b=1, x=1):
    while a > 0:
        x *= (-0.5)
        b += x
        return row_num(a - 1, b, x)
    return b


print("Введите кол-во n элементов ряда чисел для вычисления суммы ")
n = int(input("n = ")) - 1
print(f"Сумма n = {n + 1} элементов ряда чисел вида 1, -0.5, 0.25, -0.125,… равна  {row_num(n)}")

