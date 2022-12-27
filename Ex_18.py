# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

while True:
    try:
        import random

        n = int(input('Введите значение N: '))
        x = int(input('Введите значение X: '))

        m = []
        for num in range(n):
            random_number = round(random.uniform(1, n), 0)
            m.append(int(random_number))

        print(m)

        def nearest_value(list, x):
            found = list[0]        
            for item in list:     
                if abs(item - x) < abs(found - x):     
                    found = item 
            return found 
        
        print(f'Ближайшее число к {x} в массиве {m} является {nearest_value(m, x)}')
        break
    except:
        print('Ошибка! Необходимо ввести целое положительное число')


