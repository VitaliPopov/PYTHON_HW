'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


5
1 2 3 4 5
3
-> 1
'''
import random
N = int(input("Enter list size: "))
#print(N)
#X = int(input("Enter number: "))
# print(X)
list_1 = []
for i in range(N):
    number = random.randint(0, 10)
    list_1.insert(0, number)
print(N)
print(*list_1)
X = int(input("Enter number: "))
print(X)
count = 0
for item in list_1[0:]:
    if X == item:
        count += 1
print(count)
