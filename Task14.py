'''
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
'''
N = int(input("Enter number: "))
degree = 1
k = 0
a = 2

while degree<N:
    k += 1
    print(degree, end=' ')
    degree = a ** k
