
def num_translate(num):
    if num in numbers.keys():
        return numbers[num]
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
print(num_translate('ten'))
