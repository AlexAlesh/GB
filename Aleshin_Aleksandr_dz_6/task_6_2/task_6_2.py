from requests import get

address = get('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text
with open('spam.txt', 'w', encoding='utf-8') as f:
    f.write(address)
name = {}
with open('spam.txt', 'r', encoding='utf-8') as f:
    for line in f:
        pars = line.replace('"', '').split(' ')
        name.setdefault(pars[0], 0)
        name[pars[0]] += 1
max_val = max(name.values())
max_key = max(name, key=name.get)
print(f'IP адрес вредителя: {max_key}\nКоличество запросов вредителя: {max_val}')
