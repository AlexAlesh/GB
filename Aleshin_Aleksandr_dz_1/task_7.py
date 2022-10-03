# палиндром

from task_14 import DequeClass


def pal_checker(string):
    dc_obj = DequeClass()

    for el in string.replace(' ', ''):  # вот и все))
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal


print(pal_checker("молоко делили ледоколом"))
print(pal_checker("топот"))
