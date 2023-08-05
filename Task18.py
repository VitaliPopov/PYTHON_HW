'''
Задача 18: Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


5
1 2 3 4 5
6

-> 5
'''

import random
N = int(input("Enter list size: "))
#print(N)
#X = int(input("Enter number: "))
# print(X)
flag = True
list_1 = []
for i in range(N):
    number = random.randint(0, 10)
    list_1.insert(0, number)
print(N)
print(*list_1)
k = int(input("Enter number: "))
print(k)

found = list_1[0]        # принимаем допущение что ближайшее число к искомому первое в списке (с индексом 0)
for item in list_1:      # для каждого элемента (item) из items (т.е. попеременно item=1, item=2..)
        # проверяем условие если разница между item value по модулю меньше разницы found и value, то
    if abs(item - k) < abs(found - k): # если условие истинно (True)
        found = item # меняем значение нашего допущения на item (т.е. item оказался ближе к искомому значению)
flag = False
print(found)