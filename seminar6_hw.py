"""
Задача 30:  Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""

# first = int(input("Первый элемент прогрессии "))
# difference = int(input("Разность "))
# count = int(input("Количество элементов "))

# l = list()
# for i in range(1, count + 1):
#     l.append((first + (i-1)*difference))

# print(l)

"""
Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""

from random import randint

MinValue = int(input("Минимальный элемент "))
MaxValue = int(input("Максимальный элемент "))

l = [randint(1, 100) for _ in range(20)]
indexes = []
for i in range(len(l)):
    if MinValue <= l[i] <= MaxValue:
        indexes.append(i)

print(l)
print(indexes)

