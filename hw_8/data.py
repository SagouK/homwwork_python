import json

def save(employees):
    with open('base.json','w',encoding='utf-8') as bs:
        bs.write(json.dumps(employees,ensure_ascii=False))
    print('Наша БД успешно сохранена в файле base.json')

def load():
    with open('base.json','r',encoding='utf-8') as bs:
        employees = json.load(bs)
    print('Наша БД успешно загружена')
    return employees