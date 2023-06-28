
"""
Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. 
Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.

Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, 
и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), 
то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы

Формат входных данных
В первой строке подаётся число 
n
n – количество холодильников. В последующих 
n
n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 
5
5 до 
100
100 символов.

Формат выходных данных
Программа должна вывести номера зараженных холодильников через пробел. 
Если таких холодильников нет, ничего выводить не нужно.

Формат входных данных
В первой строке подаётся число 
n
n – количество холодильников. В последующих 
n
n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 
5
5 до 
100
100 символов.

Формат выходных данных
Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.

Sample Input 1:
6
222anton456
a1n1t1o1n1
0000a0000n00t00000o000000n
gylfole
richard
ant0n
Sample Output 1:
1 2 3
Sample Input 2:
9
osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
anton
aoooooooooontooooo
elelelelelelelelelel
ntoneeee
tonee
253235235a5323352n25235352t253523523235oo235523523523n
antoooooooooooooooooooooooooooooooooooooooooooooooooooon
unton
Sample Output 2:
1 2 7 8
"""

inp = "elelelelelelelelelel"
etalon = "anton"

# Вариант 5

# istrue = True
# startindex = 0
# for i in etalon:
#     try:
#         startindex = inp.index(i, startindex)
#     except:
#         istrue = False
#         break
# print(istrue)

# Вариант 4

i = 0
istrue = False
while len(inp) > 0:
    if inp.startswith(etalon[i]):
        i += 1
        if i == len(etalon):
            istrue = True
            break
    inp = inp[1:]
print(istrue)

#  Вариант 3
# i = 0
# istrue = False
# while len(inp) > 0:
#     if inp[0] == etalon[i]:
#         i += 1
#         if i == len(etalon):
#             istrue = True
#             break
#     inp = inp[1:]
# print(istrue)

# Вариант 2
# istrue = True
# for i in etalon:
#     if inp[0] == i:
#         inp = inp[1:]
#     else:
#         a = inp.split(i, 1)
#         if len(a) == 1:
#             istrue = False
#             break
#         inp = a[1]
# print(istrue)

# Вариант 1
# i = 0
# inp = list(inp)
# istrue = False
# while len(inp) > 0:
#     if inp.pop(0) == etalon[i]:
#         i += 1
#         if i == len(etalon):
#             istrue = True
#             break
# print(istrue)

