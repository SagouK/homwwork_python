
import view
import logger
import functions
import data

def start_system(employees):
    while True:
        choose_function = view.view_menu()
        if choose_function == 1:
            employee = functions.add_employee()
            employees.append(employee)
            print('Сотрудник добавлен!')
            logger.write_info_add_employee('Добавили сотрудника')

        elif choose_function == 2:
            functions.del_employee(employees)
            logger.write_info_add_employee('Удалили сотрудника')

        elif choose_function == 3:
            functions.search_data_employee(employees)

        elif choose_function == 4:
            functions.print_all_employees(employees)
            logger.write_info_add_employee('Вывели весь список сотрудников на экран')

        elif choose_function == 5:
            print('Вы остановили программу.')
            logger.write_info_add_employee('Остановили программу')
            break

        elif choose_function == 6:
            data.save(employees)
            print('Вы сохранили изменения')
            logger.write_info_add_employee('Сохранили изменения')
        else: 
            print('Неопознанная команда. Пожалуйста, ознакомтесь со списком доступных команнд через команду "/help".')
