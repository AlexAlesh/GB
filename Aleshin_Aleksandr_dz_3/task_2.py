"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш
Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей
ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""
import hashlib
import json
import os.path

class Hash:

    @staticmethod
    def users():
        login = input("Логин: ")
        password = input("Пароль: ")
        hash = hashlib.sha256(login.encode() + password.encode()).hexdigest()
        return login, hash

    def create_json(self):
        file_path = 'db2.json'
        if os.path.exists(file_path) == True:
            return self.add_to_json()
        else:
            login, pas = self.users()
            json_data = {login: pas}
            with open('db2.json', 'w') as file:
                file.write(json.dumps(json_data, indent=1, ensure_ascii=False))
            return login, pas

    def add_to_json(self):
        login, pas = self.users()
        json_data = {login: pas}
        data = json.load(open("db2.json"))
        data.update(json_data)
        with open("db2.json", "w") as file:
            json.dump(data, file, indent=1, ensure_ascii=False)
        return login, pas

    def regist(self):
        f = open('db2.json')
        data = json.load(f)
        f.close()
        login, pas = self.users()
        flag = 0
        for val in data.values():
            if val == pas:
                return 'Вы зарегистрированны'
            else:
                flag = 1
        if flag == 1:
            if 'y' == input('Хотите загеристирироваться? (y/n)'):
                return self.add_to_json()
            else:
                return 'Всего доброго'
query = Hash()
#print(query.create_json())
print(query.regist())

