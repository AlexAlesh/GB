user = []
hobby = []
with open('users.txt', 'r', encoding='utf-8') as f:
    for u in f:
        user.append(u.replace('\n', ''))
with open('hobby.txt', 'r', encoding='utf-8') as f:
    for h in f:
        hobby.append(h.replace('\n', ''))
final = []
for i in range(len(user)):
    dict_in = {user[i]: hobby[i] if i < len(hobby) else None}
    final.append(dict_in)
with open('final.txt', 'w', encoding='utf-8') as f:
    if len(hobby) > len(user):
        print('1')
        f.write('ошибка: код 1')
    else:
        for i in final:
            f.write(str(i) + '\n')
