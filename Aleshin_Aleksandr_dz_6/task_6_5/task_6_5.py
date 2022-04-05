from itertools import zip_longest
user = []
hobby = []
with open(input('Введите название файла с пользователями \n например "users.txt": '), 'r', encoding='utf-8') as f:
    for u in f:
        user.append(u.replace('\n', ''))
with open(input('Введите название файла с хобби \n например "hobby.txt": '), 'r', encoding='utf-8') as f:
    for h in f:
        hobby.append(h.replace('\n', ''))
with open(input('Создание файла, название файла с расширением "txt": '), 'w', encoding='utf-8') as f:
    if len(hobby) > len(user):
        print('1')
        f.write('ошибка: код 1')
    else:
        for users, hobbys in zip_longest(user, hobby):
            print('файл успешно создан')
            f.write(f'{users} : {hobbys} \n')
