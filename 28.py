# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(a, b):
    if b == 0:
        return a
    else:
        return a+sum(1, b-1)
a = int(input("Введите первое слагаемое: "))
b = int(input("Введите второе слагаемое: "))
print("{} + {} = {}".format(a, b, sum(a,b)))