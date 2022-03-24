from random import choice


def get_jokes(quiry_int, quiry='y'):
    """
    Кладец шуток прибауток
    :param quiry_int: количество шуток
    :param quiry: можно ли повторять слова
    :return: список с шутками
    """
    i = 0
    control = len(nouns)
    ls = []
    while quiry_int > i:
        if quiry == 'y':
            jokes = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)} '
            ls += [jokes]
        elif quiry == 'n':
            noun = choice(nouns)
            adverb = choice(adverbs)
            adjective = choice(adjectives)
            jokes = f'{noun} {adverb} {adjective} '
            ls += [jokes]
            nouns.remove(noun), adverbs.remove(adverb), adjectives.remove(adjective)
            if len(ls) >= control:
                ls += ['УПС! Мой словарный запас иссяк :( ']
        i += 1
    return ls


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

quiry_int = int(input('Сколько шуток сформировать? '))

print(get_jokes(quiry_int, quiry='n'))
