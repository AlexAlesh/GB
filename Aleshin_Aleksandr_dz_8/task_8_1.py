import re

buffer = {'username': '', 'domain': ''}
RE_PRODUCTS = re.compile(r'^([a-z 1-9./-]+)[@]+([+[a-z]+[./][a-z]+)')


def email_parse(mail):
    query = RE_PRODUCTS.findall(mail.lower())
    if query:
        for pars in query:
            buffer['username'] = pars[0]
            buffer['domain'] = pars[1]
            return print(buffer)
    else:
        msg = f'wrong email: {mail}'
        raise ValueError(msg)


email_parse('someone@geekbrains.ru')
email_parse('So1me@geekbrains.ru')
email_parse('So-me@geekbrains.ru')
email_parse('So-me@geekbrainsru')





