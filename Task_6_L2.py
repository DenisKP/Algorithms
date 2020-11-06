from random import randint

print("У вас есть 10 попыток угадать загаданное число в интервале от 0 до 100")
hid_num = int(randint(0, 100))
for i in range(10):
    us_num = int(input(f"Попытка номер {i + 1} - "))
    if us_num == hid_num:
        print("Вы угадали, Поздравляем!!!")
        break
    elif us_num > hid_num:
        print("Введенное вами число больше загаданного.  Вы не угадали.")
    else:
        print("Введенное вами число меньше загаданного. Вы не угадали.")
print(f"Было загадано число {hid_num}")
