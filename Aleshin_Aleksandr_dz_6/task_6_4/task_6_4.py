from itertools import zip_longest

with open('users.txt', 'r', encoding='utf-8') as users:
    with open('hobby.txt', 'r', encoding='utf-8') as hobby:
        with open('user_hobby.txt', 'w', encoding='utf-8') as f:
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
