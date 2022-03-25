

def thesaurus(*args):
    name = {}
    for ls in args:
        name[ls[0]] = name.setdefault(ls[0], []) + [ls]  # создаю ключи с пустым списком, в список добавляется значение
    sort_name= sorted(name.items())
    return f'{name} \n{dict(sort_name)} sort'


print(thesaurus("Мария", "Иван", "Петр", "Илья","Марина", "Анна", "Инна"))


