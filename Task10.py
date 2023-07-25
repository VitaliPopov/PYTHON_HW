'''
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
'''
import random
N = int(input("Enter coin count: "))
min_coin_turn = 0
count_avers = 0
count_revers = 0
while N != 0:
    coins = random.randint(0, 1)
    print(coins, end=' ')
    if coins >0:
        count_avers += 1
    else:
        count_revers += 1
    N -= 1
    if count_avers>count_revers:
        min_coin_turn=count_revers
    else:
        min_coin_turn=count_avers
print()
print("Минимальное число переворачиваний=  ", min_coin_turn)
#print(count_revers)
#print(count_avers)