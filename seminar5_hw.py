"""
Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
"""

def multiply(number, count):
    if count == 0:
        return 1
    elif count == 1:
        return number
    return number * multiply(number, count - 1)

print(f"3 в степени 0 = {multiply(3, 0)}")
print(f"3 в степени 1 = {multiply(3, 1)}")
print(f"3 в степени 5 = {multiply(3, 5)}")
print(f"2 в степени 3 = {multiply(2, 3)}")


"""Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
2 2
4
"""

def summa(a, b):
    if b == 0:
        return a
    return summa(a + 1, b - 1)

print(f"2 + 2 = {summa(2,2)}")
print(f"50 + 3 = {summa(50,3)}")
print(f"0 + 3 = {summa(0,3)}")
print(f"6 + 0 = {summa(6,0)}")

