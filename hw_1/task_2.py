# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def input_values(length):
    arr = []
    for i in range(length):
        num = int(input(f'Введите значение: '))
        arr.append(num)
    return arr

def check_statement(array):
    left = not (array[0] or array[1] or array[2])
    right = not array[0] and not array[1] and not array[2]
    if left == right:
        print('Истина')
    else:
        print('Ложь')
   

values = input_values(3)
check_statement(values)
   


