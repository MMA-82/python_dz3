#Задайте список из вещественных чисел. 
#Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.

import random
my_list = []
length = int(input('Задайте длину списка: '))
part_list = []
for i in range(length):
    amount = random.randint(0, 2)
    my_list.append(round(random.uniform(0, 10), amount))
    if my_list[i] %1 != 0:
        part = my_list[i] % int(my_list[i])
        part_list.append(part)
print(my_list)
print('Разница между максимальным и минимальным значением дробной части элементов, отличной от 0 =', round(max(part_list) - min(part_list), 2))

