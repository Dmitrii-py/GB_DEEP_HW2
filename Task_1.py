""" Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата."""

num = int(input('введите число: '))
check_hex = hex(num)
DIV_HEX = 16
HEX_CHAR = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
hex_res = ''
result = ''
abc_num = abs(num)
while abc_num >= 1:
    res = abc_num % DIV_HEX
    if res in HEX_CHAR:
        res = HEX_CHAR[res]
    result += str(res)
    abc_num = abc_num // DIV_HEX
    hex_res = result[::-1] if num > 0 else f'-{result[::-1]}'
print(f'наш результат: {hex_res}, функция: {check_hex}')
