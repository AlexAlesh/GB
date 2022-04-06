from itertools import zip_longest

with open(input('Введите название файла с пользователями \n например "users.txt": '), 'r', encoding='utf-8') as users:
    with open(input('Введите название файла с хобби \n например "hobby.txt": '), 'r', encoding='utf-8') as hobby:
        with open(input('Создание файла, название файла с расширением "txt": '), 'w', encoding='utf-8') as f:
            count_user = 0
            for line in users:
                count_user += 1
            count_hobby = 0
            for line in hobby:
                count_hobby += 1
            users.seek(0)
            hobby.seek(0)
            if count_hobby > count_user:
                exit(1)
            else:
                for user, hobbys in zip_longest(users, hobby):
                    if hobbys == None:
                        f.write(f'\n{user.strip()} : {hobbys}')
                    else:
                        f.write(f'{user.strip()} : {hobbys}')
