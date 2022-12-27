#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random
list = []
d = int(input('Задайте длину списка: '))
for i in range(d):
    list.append(random.randint(0, 10))
print(list)
prodlist = []
for i in range(d//2):
    prod = (list[i] * list[len(list)-1])
    prodlist.append(prod)
    list.pop()
print(prodlist)