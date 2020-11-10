def func_var(nat, a=0):
    while nat != 0:
        a += nat
        return func_var(nat - 1, a)
    return a


print("Введите множество натуральных чисел")
n = int(input("n = "))
x1 = func_var(n)
x2 = (n * (n + 1)) / 2
if x1 == x2:
    print(f" ВЫВОД Множество 1+2+...+n РАВНЫ n(n+1)/2 для n = {n} и составляют 1+2+...+n = {x1}  n(n+1)/2 = {x2}")
else:
    print(f" ВЫВОД Множество 1+2+...+n НЕ РАВНЫ n(n+1)/2 для n = {n} и составляют 1+2+...+n = {x1}  n(n+1)/2 = {x2}")
