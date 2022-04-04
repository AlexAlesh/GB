import sys
with open('bd.txt', 'r+', encoding='utf-8') as f:
    sale = f.read()
    num = tuple(sale.replace('\n', ' ').strip().split(' '))
    s_a = sys.argv[1:]
    if len(s_a) == 1:
        for i in num[int(sys.argv[1]):]:
            print(i)
    elif len(s_a) == 2:
        for i in num[int(sys.argv[1]):int(sys.argv[2])]:
            print(i)
    else:
        for i in num:
            print(i)
