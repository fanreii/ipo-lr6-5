'''Написать программу, которая:
- Создаёт с помощью генератора списков, список случайных целых чисел от **-50** до **50** размером **25** элементов.
- Находит количество положительных, отрицательных и нулевых элементов в списке.
- Выводит значения и их (*положительных, отрицательных и нулевых*) количество вместе с процентом от общего количества.
- Выводит самое большое и самое маленькое значение'''
# импорт модуля random для генерации случайных чисел
import random
# генерация списка случайных чисел диапазона -50 50 размером 25
numbs = [random.randint(-50,50) for l in range(25)]
# инициализация счетчика 
positives = 0
negatives = 0
zero = 0
# подсчет количества положительных, отрицательных и нулей
for number in numbs:
    if number > 0:
        positives += 1
    elif number < 0:
        negatives += 1
    else:
        zero += 1
# рассчет процентов
total_count = len(numbs)
positives_percentage = (positives / total_count) * 100
negatives_percentage = (negatives / total_count) * 100
zero_percentage = (zero / total_count) * 100
# нахождение наибольшего и наименьшего значения
max_val = max(numbs)
min_val = min(numbs)
# вывод результатов
print("Список чисел")
print(numbs)
print("\nРезультаты: ")
print(f"Положительные числа: {positives} ({positives_percentage}%)")
print(f"Отрицательные числа: {negatives} ({negatives_percentage}%)")
print(f"Нули: {zero} ({zero_percentage}%)")
print(f"\nСамое большое значение: {max_val}")
print(f"Самое маленькое значение: {min_val}")