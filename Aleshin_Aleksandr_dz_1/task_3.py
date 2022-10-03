"""
Задание 3.
Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


def company_list(self):
    com_key = []  # 0(1)
    com_val = []  # 0(1)
    for key, val in companies.items():  # 0(n)
        com_key.append(key)  # 0(1)
        com_val.append(val)  # 0(1)

    top = []  # 0(1)
    for i in range(3):  # O(1)
        key = com_key.pop(com_val.index(max(com_val)))  # 0(1)
        val = com_val.pop(com_val.index(max(com_val)))  # 0(1)
        top.append((key, val))  # 0(1)

    return f'первое решение: {top}'  # 0(1)


def company_zip(self):
    top = []  # 0(1)
    for i in range(3):  # 0(1)
        val = companies.get(max(companies, key=companies.get))  # 0(O(n))
        reverse = dict(zip(companies.values(), companies.keys()))  # 0(O(n))
        top.append((reverse.get(val), val))  # 0(1)
        companies.pop(reverse.get(val))  # 0(1)
    return f'второе решение: {top}'  # 0(1)



companies = {'astral': 12500.1,
             'pfr.ru': 1000000,
             'sport': 900000.8,
             'subel': 50032.12,
             'google.com': 12000,
             'vk.ru': 100500,
             'yu.ru': 1000000}


query = company_list(companies)
print(query)
print()
query = company_zip(companies)
print(query)
