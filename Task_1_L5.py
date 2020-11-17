# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий, чья прибыль выше среднего и ниже среднего.
from collections import defaultdict


def comp_info_inp(num_com):
    _earn_calc_dict = defaultdict(list)
    _average_earns = 0
    for i in range(num_com):  # input
        comp_name = input("Введите название фирмы: ")
        tot_comp_earn = 0
        for qrt in range(4):
            tot_comp_earn += int(input(f"Выручка за {qrt + 1} квартал составила: "))
        _average_earns += tot_comp_earn  # calculation of total earns
        _earn_calc_dict[comp_name].append(tot_comp_earn)
    _average_earns = _average_earns / num_com  # calculation of average earns also we can append average to dict
    _earn_calc_dict["average_earns"].append(_average_earns)
    return _earn_calc_dict, _average_earns


def who_is_who_calculations(ecd):   # calculation and result output for 2-nd task
    calc_def_dict = defaultdict(list)
    for company in ecd:
        if ecd[company] >= ecd["average_earns"] and company != "average_earns":
            calc_def_dict["more"].append(company)
        elif ecd[company] < ecd["average_earns"] and company != "average_earns":
            calc_def_dict["less"].append(company)
        else:
            pass
    return f"Компании с выручкой выше средней {calc_def_dict['more']} \n " \
           f"Компании с выручкой ниже средней {calc_def_dict['less']} "    # that return of f-stroke  valid only for
# that situation, if we want to use these data, we will return only two references to use them in latest calculations


number_of_comp = int(input("Введите кол-во фирм для подсчета: "))
earn_calc_dict, average_earns = comp_info_inp(number_of_comp)
print(f"Средняя выручка по {number_of_comp} компаниям составила - {average_earns}")   # 1-st task print average earns
print(who_is_who_calculations(earn_calc_dict))  # 2-nd task print who has more or less earns from average.
