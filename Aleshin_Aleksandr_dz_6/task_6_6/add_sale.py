with open('bd.txt', 'a', encoding='utf-8') as f:
    shop = input('внесите сумму продажи: ')
    f.writelines(str(shop) + '\n')
