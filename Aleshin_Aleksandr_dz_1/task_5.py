
class StackClass:
    def __init__(self):
        self.elems = []
        self.array = []

    def is_array(self):
        size = len(self.elems)
        if size > 5:
            while len(self.elems) > 0:
                if len(self.elems) > 5:
                    self.array.append(self.elems[:5])
                    del self.elems[:5]
                else:
                    self.array.append(self.elems)
                    return f'Сторки:{self.array}\nКоличество стопок: {len(self.array)}\nКоличество элементов: {size}'
        return f'Сторки:{self.array}\nКоличество стопок: {len(self.array)}\nКоличество элементов: {size}'

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        self.elems.append(el)

    def pop_out(self):
        if len(self.array[-1]) > 0:
            self.elems = self.array[-1]
            return self.elems.pop()
        else:
            del self.array[-1]

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


if __name__ == '__main__':

    SC_OBJ = StackClass()

    print(SC_OBJ.is_empty())  # -> стек пустой

    # наполняем стек
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    print()
    print(SC_OBJ.is_array())
    print()
    # получаем значение первого элемента с вершины стека,
    # но не удаляем сам элемент из стека
    print(SC_OBJ.get_val())  # -> 5.5

    # узнаем размер стека
    print(SC_OBJ.stack_size())  # -> 4

    print(SC_OBJ.is_empty())  # -> стек уже непустой

    # кладем еще один элемент в стек
    SC_OBJ.push_in(4.4)

    # убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> 4.4

    # снова убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> 5.5
    print(SC_OBJ.pop_out())
    print(SC_OBJ.pop_out())
    print(SC_OBJ.pop_out())
    print(SC_OBJ.pop_out())
    # вновь узнаем размер стека
    print(SC_OBJ.stack_size())  # -> 3
    print(SC_OBJ.is_array())