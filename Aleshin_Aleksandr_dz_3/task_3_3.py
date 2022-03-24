

def thesaurus(*args):
    name = {}
    for ls in args:
        name.setdefault(ls[0], []) # создаю ключи с пустым списком
        name[ls[0]] += [ls]  # прибавляю значения по ключам
    sort_name= sorted(name.items())
    return f'{name} \n{dict(sort_name)} sort'
print(thesaurus("Мария", "Иван", "Петр", "Илья","Марина", "Анна", "Инна"))


