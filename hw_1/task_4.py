#Напишите простой калькулятор, который считывает с пользовательского ввода три строки: 
# первое число, второе число и операцию, после чего применяет операцию к введённым числам 
# ("первое число" "операция" "второе число") и выводит результат на экран.

#Поддерживаемые операции: +, -, /, *, mod, pow, div, где
#mod — это взятие остатка от деления,
#pow — возведение в степень,
#div — целочисленное деление.

def calculator(a, procedure, b):
    if procedure == '+':
        result = a + b
    elif procedure == '-':
        result = a - b
    elif procedure == '/' and b !=0:
        result = a / b
    elif procedure == '/' and b == 0:
        print('Деление на 0 невозможно')
    elif procedure == '*':
        result = a * b
    elif procedure == 'mod':
        result = a % b
    elif procedure == 'mod' and b == 0:
        print('Деление на 0 невозможно')
    elif procedure == 'pow':
        result = a ** b
    elif procedure == 'div':
        result = a // b
    elif procedure == 'div' and b == 0:
        print('Деление на 0 невозможно')
    else:
        print('Введите поддерживаемую операцию!')
    return result
    
try:
    first_num = float(input('Введите первое число: '))
    operation = input('Введите применяемую операцию: ')
    second_num = float(input('Введите второе число: '))
    print(calculator(first_num, operation, second_num))
except:
    print('Ошибка ввода данных!')

    