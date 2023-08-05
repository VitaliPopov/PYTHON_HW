'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
'''
#import random
import intersection
N = int(input("Enter list_1 size: "))
list_1 = []
for i in range(N):
    # number = random.randint(0, 10)
    # list_1.insert(0, number)
    number = int(input('Enter number:'))
    list_1.append(number)
#print(N)
print(*list_1)
new_list_1 = sorted(list_1)
print(new_list_1)
unique_numbers_new_list_1 = list(set(new_list_1))
print(unique_numbers_new_list_1)
M = int(input("Enter list_2 size: "))
list_2 = []
for i in range(M):
    # number = random.randint(0, 10)
    # list_2.insert(0, number)
    number = int(input('Enter number:'))
    list_2.append(number)
print(M)
print(*list_2)
new_list_2 = sorted(list_2)
print(new_list_2)
unique_numbers_new_list_2 = list(set(new_list_2))
print(unique_numbers_new_list_2)
unique_numbers_found = sorted(unique_numbers_new_list_1 + unique_numbers_new_list_2)
print(unique_numbers_found)
same_numbers_list = []
for item in unique_numbers_found:
        if unique_numbers_found.count(item) > 1 and item not in same_numbers_list:
            same_numbers_list.append(item)

print(same_numbers_list)
