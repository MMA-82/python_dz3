#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random
length = int(input('Задайте длину списка: '))
list = []
for i in range(length):
    list.append(random.randint(0, 10))
print(list)
prodlist = []
for i in range(length//2):
    prod = (list[i] * list[len(list)-1])
    prodlist.append(prod)
    list.pop()
if length %2 != 0:
    prodlist.append(pow(list[len(list)//2 + 1], 2))
print(f'Произведение пар чисел: {prodlist}')