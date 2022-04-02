from requests import get

address = get('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text
with open('address.txt', 'w', encoding='utf-8') as f:
    f.write(address)
ls = []
with open('address.txt', 'r', encoding='utf-8') as f:
    for line in f:
        pars = line.replace('"', '').split(' ')
        user = pars[0], pars[5], pars[6]
        ls.append(user)
print(*ls, sep='\n')