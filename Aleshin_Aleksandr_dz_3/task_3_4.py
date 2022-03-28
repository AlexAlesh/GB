def thesaurus_adv(*args):
    surname_list = {}
    for ls in args:
        name, sur = ls.split(' ')  # разделяю имя и фамилию
        surname_list.setdefault(sur[0], {})
        surname_list[sur[0]].setdefault(ls[0], [])
        surname_list[sur[0]][ls[0]].append(ls)
    return surname_list


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))


