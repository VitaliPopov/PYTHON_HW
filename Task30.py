'''
Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов
 нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
'''

first_element = int(input('Enter firs element: '))
step_progres = int(input('Enter step: '))
count_elements = int(input('Enter elements count: '))

def progression(first_element, step_progres, count_elements):

    if count_elements == 1:
        return first_element
    
    # elif step_progres == 0:
    #     list_progr = []
    #     for i in range(count_elements):
    #         list_progr.append(first_element)
    #     return list_progr
    #elif step_progres > 0:
    
    else:
        list_progr = []
        next_element = first_element
        for i in range(count_elements):
            list_progr.append(next_element)
            next_element += step_progres
        return list_progr

print(progression(first_element, step_progres, count_elements))  
