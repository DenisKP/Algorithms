def rfu(n, e=0, o=0):
    while n > 0:
        if n % 2 == 0:
            e += 1
        else:
            o += 1
        return rfu(n // 10, e, o)
    return e, o


print("Введите любое натуральное число")
a = int(input("a = "))
evq, odq = rfu(a)
print(f"В веденном вами числе {a} Четных цифр = {evq}, Нечетных цифр = {odq}")
