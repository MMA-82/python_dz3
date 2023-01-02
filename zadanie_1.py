#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.

import random
list = []
length = int(input('Задайте длину списка: '))
sum = 0
for i in range(length):
    list.append(random.randint(0, 10))
    if i % 2 == 1:
        sum += list[i]
print(list)
print('Сумма элементов списка с нечетным индексом =', sum)

    
