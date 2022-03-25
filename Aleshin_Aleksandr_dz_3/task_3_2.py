
def num_translate_adv(num):
    if num == num.lower():
        if num in numbers.keys():
            return numbers[num]
        else:
            return numbers.get(num)
    elif num == num.capitalize():
        num = num.lower()
        if num in numbers.keys():
            lower = numbers[num]
            return lower.capitalize()
        else:
            return numbers.get(num)


numbers = {'one': 'один',
           'two': 'два',
           'three': 'три',
           'four': 'четыре',
           'five': 'пять',
           'six': 'шесть',
           'seven': 'семь',
           'eight': 'восемь',
           'nine': 'девять',
           'ten': 'десять'
           }

print(num_translate_adv('ten'))
print(num_translate_adv('Five'))

