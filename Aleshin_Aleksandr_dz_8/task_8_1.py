import re

RE_PRODUCTS = re.compile(r'^(?P<username>[a-z1-9./]+)@(?P<domain>[+[a-z]+[./][a-z]+)$')


def email_parse(mail):
    query = RE_PRODUCTS.findall(mail.lower())
    if query:
        print(*map(lambda x: x.groupdict(), RE_PRODUCTS.finditer(mail.lower())), sep=',')
    else:
        msg = f'wrong email: {mail}'
        raise ValueError(msg)


email_parse('someone@geekbrains.ru')
email_parse('So1me@geekbrains.ru')
email_parse('So.me@geekbrains.ru')
email_parse('So-me@geekbrainsru')





