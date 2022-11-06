import view
import controller
import json

def add_employee():
    lastname = input('Введите фамилию сотрудника: ')
    firstname = input('Введите имя сотрудника: ')
    birth_day = input('Введите дату рождения сотрудника: ')
    position = input('Введите должность сотрудника: ')
    time_work = input('Введите стаж работы сотрудника: ')
    home_place = input('Введите место жительства сотрудника: ')
    phone_number = input('Введите телефон сотрудника: ')
    data_base = {'Фамилия': lastname, 'Имя': firstname, 'Дата рождения': birth_day, 'Должность': position, 'Стаж работы': time_work, 'Место жительства': home_place, 'Личный телефон': phone_number}
    return data_base

def del_employee(employees):
    delete_person = input('Введите фамилию сотрудника, которого хотите удалить: ')
    try:
        for i in employees:
            if i["Фамилия"] == delete_person:
                employees.remove(i)
                print('Сотрудник был успешно удален.')
                break
    except:
        print('Такого сотрудника нет в базе данных, либо вы ввели фамилию с маленькой буквы!')

def search_data_employee(employees):
    try:
        person_last = input('Введите фамилию сотрудника, данные которого вы хотите найти. ')
        person_first = input('Введите имя сотрудника, данные которого вы хотите найти. ')
        print('Данные сотрудника:\n\
        1. Дата рождения.\n\
        2. Должность.\n\
        3. Стаж работы.\n\
        4. Место жительства.\n\
        5. Телефон.\n\
        6. Все данные.\n\
        7. Закрыть меню.')
        while True:
            data_search = int(input('Введите, пожалуйста, нужную цифру, соответствующую функции в меню. '))
            if data_search == 1:
                for i in employees:
                    if person_last == i['Фамилия'] and person_first == i['Имя']:
                        print(i['Дата рождения'])
            elif data_search == 2:
                for i in employees:
                    if person_last == i['Фамилия'] and person_first == i['Имя']:
                        print(i['Должность'])
            elif data_search == 3:
                for i in employees:
                    if person_last == i['Фамилия'] and person_first == i['Имя']:
                        print(i['Стаж работы'])
            elif data_search == 4:
                for i in employees:
                    if person_last == i['Фамилия'] and person_first == i['Имя']:
                        print(i['Место жительства'])
            elif data_search == 5:
                for i in employees:
                    if person_last == i['Фамилия'] and person_first == i['Имя']:
                        print(i['Личный телефон'])
            elif data_search == 6:
                for i in employees:
                    if person_last == i['Фамилия'] and person_first == i['Имя']:
                        print(i)
            elif data_search == 7:
                False
                break
    except:
        print('Такого сотрудника нет.')

def print_all_employees(employees):
    print('Вот текущий список сотрудников.\n')
    for i in employees:
        print(f'{i["Фамилия"]} {i["Имя"]}\n')
