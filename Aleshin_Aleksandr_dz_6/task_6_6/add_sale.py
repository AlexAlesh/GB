with open('bd.txt', 'a', encoding='utf-8') as f:
    shop = float(input('внесите сумму продажи типа <8914.3>: '))
    f.writelines(str(shop) + '\n')
