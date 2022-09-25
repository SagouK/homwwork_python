# Напишите программу, которая принимает на вход координаты точки 
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

def quarter_number(x, y):
    if x > 0 and y > 0:
        print('1')
    elif x < 0 and y > 0:
        print('2')
    elif x < 0 and y < 0:
        print('3')
    else:
        print('4')
try:
    num_1 = int(input('Введите Х: '))
    num_2 = int(input('Введите Y: '))
    if num_1 != 0 and num_2 != 0:
        quarter_number(num_1, num_2)
    else:
        print('Координаты должны быть не равны 0!')
except:
    print('Ошибка ввода данных!')