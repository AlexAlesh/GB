
class StackClass:
    def __init__(self):
        self.a_task = []
        self.revision = []
        self.solution = []

    def is_empty(self):
        return self.a_task == []

    def push_in(self, el):
        self.a_task.append(el)

    def pop_out_task(self):
        if input('задача решена? (y/n) ') == 'n':
            self.revision.append(self.a_task.pop())
            return self.revision
        self.solution.append(self.a_task.pop())
        return self.solution

    def pop_out_revision(self):
        self.solution.append(self.revision.pop())
        return f'Решенная задача {self.solution[-1]}\nосталось задач:{self.revision}'

    def get_val(self):
        return self.a_task[len(self.a_task) - 1]

    def stack_size(self):
        return len(self.a_task)


if __name__ == '__main__':

    SC_OBJ = StackClass()

    print(SC_OBJ.is_empty())  # -> стек пустой

    # наполняем стек
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)
    SC_OBJ.push_in(55)
    SC_OBJ.push_in(58)
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
    print(SC_OBJ.pop_out_task())  # -> 4.4

    # снова убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out_task())  # -> 5.5
    print(SC_OBJ.pop_out_task())
    print(SC_OBJ.pop_out_task())
    print(SC_OBJ.pop_out_revision())
    # вновь узнаем размер стека
    print(SC_OBJ.stack_size())  # -> 3
