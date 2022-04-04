user = []
hobby = []
with open('users.txt', 'r', encoding='utf-8') as f:
    for u in f:
        user.append(u.replace('\n', ''))
with open('hobby.txt', 'r', encoding='utf-8') as f:
    for h in f:
        hobby.append(h)
with open('user_hobby.txt', 'w', encoding='utf-8') as f:
    if len(hobby) > len(user):
        print('1')
        f.write('ошибка: код 1')
    else:
        for users, hobbys in zip(user, hobby):
            f.write(f'{users} : {hobbys}')
