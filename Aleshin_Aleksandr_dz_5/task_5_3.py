from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Станислав', ' Виктор']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def school(tutor, klasse):
    for i in range(len(tutor)):
        yield tutor[i], klasse[i] if i < len(klasses) else None


print(type(school(tutors, klasses)))
tut_klas = school(tutors, klasses)
print(*tut_klas, sep=('\n'))

print(*tut_klas, 'повторный вызов', sep=('\n'))

print('\n')

school_2 = (i for i in zip_longest(tutors, klasses))
print(type(school_2))
print(*school_2, sep=('\n'))

print(*school_2, 'повторный вызов', sep=('\n'))










