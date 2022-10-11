"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет
Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}
Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""
from uuid import uuid4
import hashlib
import time

#salt = uuid4().hex
test = time.time()
#print(salt)
#print(test)
hash = {}

def internet(url):
    if hash.get(url):
        return f'данный {url} занесен'
    else:
        hash[url] = hashlib.sha256(str(test).encode() + url.encode()).hexdigest()
    return hash

query = internet
print(query('https://www.google.com/'))
print(query('https://www.google.com/'))
print(query('https://www.ya.ru/'))