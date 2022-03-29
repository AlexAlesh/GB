from decimal import Decimal
from requests import get, utils
from datetime import datetime


def currency_rates(money):
    """
    Если запрос встречается в строке
    номинал: ищется '<Nominal>', находится его первый индекс, прибавляется длина '<Nominal>'
    чтоб найти индекс последнего символа
    далее индекс '</Nominal>' и получаем символ между '<Nominal>' и '</Nominal>'
    :param money: Какую искать валюту
    :return: сколько стоит одна единица валюты в рублях
    """
    address = get('http://www.cbr.ru/scripts/XML_daily.asp').text.split("<Valute")
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    money = money.upper()
    for i in address:
        if i.count(money):
            nominal = (int(i[i.find('<Nominal>') + len('<Nominal>'):i.find('</Nominal>')]))
            value = (float(i[i.find('<Value>') + len('<Value>'):i.find('</Value>')].replace(',', '.')))
            value = Decimal(str(value))
            dt = response.headers['Date']
            dt = ' '.join(dt.split()[:-1])
            dt = datetime.strptime(dt, "%a, %d %b %Y %H:%M:%S")
            return print(f"{dt.date()}\n{nominal} {money} = {value} рублей")


if __name__ == '__main__':
    currency_rates('GBP')

