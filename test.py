# Управляющие конструкции
i = 0
if i == 45:
    print('i is 45')
elif i == 35:
    print('i is 35')
else:
    print('i is unknown')

for i in range(4):
    x = i*2  
    if i == 3:
        continue
    print(x) 

count = 0
while count < 3:
    print(f"The count is {count}")
    count += 1

# ООП
class FancyCar():
    # Добавляем переменную класса
    wheels = 4
    # Добавляем метод
    def driveFast(self):
        print("Driving so fast")

# Создаем экземпляр воображаемого автомобиля
my_car = FancyCar()
# Обращаемся к атрибуту класса
print(my_car.wheels)
my_car.driveFast()

# Последовательности

# Операторы "in" и "not in"
2 in [1,2,3]
'a' not in 'cat'
10 in range(12)
0 not in range(2, 4)

my_sequence = 'Bill Cheatham'
# Обращение по индексу
my_sequence[0] # Первый элемент
my_sequence[1] # Второй элемент
my_sequence[-1] # Последний элемент
my_sequence[-2] # Предпоследний элемент
# Получить первое вхождение элемента в последовательность
my_sequence.index('C') # 5
my_sequence.index('a',9, 12) # Поиск с указанием диапазона
# Получить срез [start:stop:step*]
my_sequence = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] # Полный срез
my_sequence[2:5] # Срез со 2 по 5 элементы
my_sequence[-6:] # Отсчитать 6 элемент с конца и продолжить срез "['b', 'c', 'd', 'e', 'f', 'g']"
my_sequence[3:-1] # Срез от 4го до последнего элемента ['d', 'e', 'f']
# Базовые функции
my_sequence = [0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4]
len(my_sequence) # Получить длину последовательности
min(my_sequence) # Получить наименьший элемент
max(my_sequence) # Получить наибольший элемент
my_sequence.count(1) # Получить номер конкретного элемента

# Списки
list()
list(range(5)) # [0, 1, 2, 3, 4]
list("Choco Pie") # ['C''h''o''c''o'' ''P''i''e']
empty = [] # Создать пустой список
three = [0, 1, 2] # Создать список со значениями
mixed = [0, 'a', empty, 'WheelHoss'] # Создать список со разнородными значениями

pies = ['cherry', 'apple']
pies.append('rhubarb') # Добавить элемент в конец (быстро!)
pies.insert(1, 'cream') # Добавить элемент в указанную позицию (медленно!)

desserts = ['cookies', 'paste']
desserts.extend(pies) # Добавить аргумент-список к концу текущего списка

pies.pop() # Получить элемент из конца и удалить его (быстро!)
pies.pop(1) # Получить элемент из позиции и удалить его (медленно!)

pies.remove('apple') # Удалить первое вхождение элемента

squares = [i*i for i in range(10)] # cписковые включения - for в одну строку
squares = [i*i for i in range(10) if i%2==0] # cписковые включения с условием

