import re
from requests import get

RE_ADDRESS = re.compile('([\S*.]+)[\s-]*\[(.*)]\s*\"(\w*)\s*(\w*\S*)[^\"]*\"\s+(\d+)\s+(\d+)')
address = get('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text

with open('address.txt', 'w', encoding='utf-8') as f:
    f.write(address)
with open('address.txt', 'r', encoding='utf-8') as f:
    with open('save.txt', 'w', encoding='utf-8') as s:
        for line in f:
            address = RE_ADDRESS.findall(line)
            save = str(address) + '\n'
            s.write(save)
