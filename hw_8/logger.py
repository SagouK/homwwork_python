import datetime

def write_info_add_employee(data):
    now = datetime.datetime.now()
    with open('log.csv', 'a', encoding = 'utf-8') as file:
        file.write('{}; {}\n'
                    .format(now, data))
