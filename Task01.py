# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль (try except).

# Пример:
# Введите первое число: 10
# Введите второе число: 0
# Вы что? Пытаетесь делить на 0!

# Process finished with exit code 0

# Пример:
# Введите первое число: 10
# Введите второе число: 10
# 1.0

# Process finished with exit code 0

my_first = int(input('Введите число 1: '))
my_second = int(input('Введите число 2: '))


def go_devide(arg_1, arg_2):
    try:
        arg_1/arg_2 or arg_2/arg_1
    except ZeroDivisionError:
        print('Вы что, пытаетесь делить на 0?!')
    else:
        print(arg_1/arg_2)


go_devide(my_first, my_second)
