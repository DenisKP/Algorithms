def find_sum(a, b=0):
    while a > 0:
        b += a % 10
        return find_sum(a // 10, b)
    return b


print('Введите натуральное число для выхода введите 0')
max_sum = 0
cur_sum = 0
nat_dig = 1
max_nat_dig = 1
while nat_dig != 0:
    nat_dig = int(input("Вводите "))
    cur_sum = find_sum(nat_dig)
    if cur_sum > max_sum:
        max_sum = cur_sum
        max_nat_dig = nat_dig
    else:
        cur_sum = 0
print(f"Среди натуральных чисел, которые были введены, наибольшее по сумме цифр от натурального числа ({max_nat_dig})"
      f" = {max_sum}")
