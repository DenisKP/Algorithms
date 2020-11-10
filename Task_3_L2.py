def check_null_in_end(a):
    while a % 10 == 0:
        a //= 10
    return a


def rev_ord(a, ro=""):
    while a > 0:
        b = a % 10
        ro += str(b)
        return rev_ord(a // 10, ro)
    return int(ro)


print("Введите любое натуральное число")
nat_dig = check_null_in_end(int(input("a = ")))
print(f" Обратное число от введенного -> {rev_ord(nat_dig)}")
