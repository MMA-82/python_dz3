#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

index = int(input('Введите коэффициент: ')) 
my_list = []
for i in range(index+1):
    my_list.append(fib(i))
    if i > 0:
        my_list.insert(0, fib(i)*pow(-1, i+1))
print(*my_list, sep=', ')