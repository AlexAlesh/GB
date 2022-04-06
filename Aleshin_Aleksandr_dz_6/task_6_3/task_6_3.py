import json
user = []
hobby = []
with open('users.txt', 'r', encoding='utf-8') as f:
    for u in f:
        user.append(u.replace('\n', ''))
with open('hobby.txt', 'r', encoding='utf-8') as f:
    for h in f:
        hobby.append(h.replace('\n', ''))
if len(hobby) > len(user):
    exit(1)
dict_in = {}
for i in range(len(user)):
    dict_in[user[i]] = hobby[i] if i < len(hobby) else None

with open('task3.json', 'w', encoding='utf-8') as f:
    json.dump(dict_in, f, ensure_ascii=False)

