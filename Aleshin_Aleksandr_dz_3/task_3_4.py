def thesaurus_adv(*args):
    surname_list = {}
    for ls in args:
        name, sur = ls.split(' ')  # разделяю имя и фамилию
        surname_list.setdefault(sur[0], {})
        surname_list[sur[0]].setdefault(ls[0], [])
        surname_list[sur[0]][ls[0]].append(ls)
    return surname_list


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))

















# # dict_out[name[0]] = list(filter(lambda el: el[0] == name[0], args))
# nums = ['0', 'Samsung Galaxy', '15.5', '18,1', 'iPhone', '748', 'HelloWord']
# int_nums = list(filter(str.isdigit, nums))
# print(int_nums) # ['iPhone', 'HelloWord']
#
#
# names = ["Майа", "Дарси", 'Макс', "Макс"]
#
# names_dict_set = dict()
# names_dict_list = dict()
#
# for name in names:
#   first_letter = name[0]
#
#   names_dict_set[first_letter] = names_dict_set.setdefault(first_letter, set()) | {name.capitalize()}
#
#   names_dict_list[first_letter] = names_dict_list.setdefault(first_letter, []) + [name.capitalize()]
#
# print(names_dict_set, names_dict_list, sep='\n')
#
# str = "это строковый пример....!!!"
#
# print ("str.capitalize() : ", str.capitalize())
