"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
Пример:
Ввод: 1/2 1/3 Вывод:5/6 1/6
"""
from fractions import Fraction


def check_result(fraction_one, fraction_two):
    f_one = Fraction(fraction_one)
    f_two = Fraction(fraction_two)
    print(f'проверка через модуль "Fraction"'
          f'\nсложение: {f_one + f_two}, произведение: {f_one * f_two}')


def operations_on_fractions(fraction_one, fraction_two):
    a = fraction_one.split('/')
    b = fraction_two.split('/')
    product_of_fractions = f'{int(a[0]) * int(b[0])}/{int(a[1]) * int(b[1])}'
    common_divisor = int(a[1]) * int(b[1])
    sum_of_fractions = f'{str((int(a[0]) * int(b[1])) + (int(b[0]) * int(a[1])))}/{str(common_divisor)}'

    print(f'{fraction_one} + {fraction_two} = {sum_of_fractions}'
          f'\n{fraction_one} * {fraction_two} = {product_of_fractions}')


one = input('Введите первую дробь в формате a/b: ')
two = input("Введите вторую дробь в формате a/b: ")
operations_on_fractions(one, two)
check_result(one, two)
