# 5. Сделайте профилирование кода любого или любых выполненных заданий
# с помощью модуля timeit, опишите результат

from timeit import timeit

num_1 = int(input('Введите число 1: '))
num_2 = int(input('Введите число 2: '))
num_3 = int(input('Введите число 3: '))


def my_func_with_sort(arg_1, arg_2, arg_3):
    a = arg_1, arg_2, arg_3
    b = sorted(a)
    return b[1]+b[2]


print(f'С sort(): {my_func_with_sort(num_1, num_2, num_3)}')


print(timeit("my_func_with_sort(num_1, num_2, num_3)", globals=globals(), number=1000))


def my_func_without_sort(arg_1, arg_2, arg_3):
    my_list = [[arg_1], [arg_2], [arg_3]]
    my_max = max(my_list)

    for i in my_list:
        if my_max == i:
            my_list.remove(i)

    my_second_max = max(my_list)

    return my_max[0]+my_second_max[0]


print(f'Без sort(): {my_func_without_sort(num_1, num_2, num_3)}')

print(timeit('my_func_without_sort(num_1, num_2, num_3)',
      globals=globals(), number=1000))

print('С sort() Работает значительно быстрее.')
