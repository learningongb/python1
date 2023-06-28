"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.

11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
"""

# set1 = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
# set2 = [3, 6, 9, 12, 15, 18]

from random import randint
from unittest import result

len1 = int(input("Размер первого набора "))
len2 = int(input("Размер второго набора "))

list1 = list()
for _ in range(len1):
    list1.append(randint(1, 10))
list2 = list()
for _ in range(len2):
    list2.append(randint(1, 10))

new_set1 = set(list1)
new_set2 = set(list2)

print("Первый набор = ", *new_set1)
print("Второй набор = ", *new_set2)

result_set = set()
for i in new_set1:
    if i in new_set2:
        result_set.add(i)
result = list(result_set)
result.sort()
print(*result)

"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai
 ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.

4 -> 1 2 3 4
9
"""
# from random import randint

# bush_count = 10
# bushs = []
# for _ in range(bush_count):
#     bushs.append(randint(0, 10))
# max_berrys = 0
# max_bush = 0

# for i in range(len(bushs)):
#     sum = bushs[i - 2] + bushs[i - 1] + bushs[i]
#     if sum > max_berrys:
#         max_berrys = sum
#         max_bush = i
# print("Вот такая грядка", *bushs)    
# print(f"Можем собрать {max_berrys} находясь перед кустом {max_bush} (нумерация с 1)")
