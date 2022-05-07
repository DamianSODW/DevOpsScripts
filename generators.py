def count(): # Функция-генератор
    n = 0
    while True:
        n += 1
        yield n # Вернуть значение и остановиться

counter = count() # Создать объект-генератор
next(counter) # Запросить следующее (первое) значение - 1
next(counter) # Запросить следующее значение - 2
next(counter) # Запросить следующее значение - 3

for x in counter:
    print(x)
    if x > 5:
        break

list_o_nums = [x for x in range(100)] # Списковое включение
gen_o_nums = (x for x in range(100)) # Генераторное включение

import sys  # Импорт пакета
sys.getsizeof(list_o_nums) # Узнать размер в байтах объекта в ОЗУ
sys.getsizeof(gen_o_nums) # Узнать размер в байтах объекта в ОЗУ