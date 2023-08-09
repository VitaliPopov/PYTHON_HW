'''
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
'''
import random
N = int(input("Enter list size: "))
list_1 = [ random.randint (-10, 10) for item in range (N)]
print(list_1)

left_number = int(input("Enter min range: "))
right_number = int(input("Enter max range: "))

def index_in_range(left_number, right_number):
    list_2 = []
    for item in range(1, N):
        if left_number <= list_1[item] and list_1[item]<= right_number:
           list_2.append(item)
    return list_2
    
print(index_in_range(left_number, right_number))
