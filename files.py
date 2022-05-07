file_path = 'bookofdreams.txt'
open_file = open(file_path, 'r') # Открыть файл в режиме чтения
text = open_file.read() # Получить сожержимое файла в виде строки
len(text) # Узнать длину всего текста
text[56] # Получить значение 57 элемента - "1 символ"
open_file.close() # Закрыть файл

open_file = open(file_path, 'r')
text = open_file.readlines() # Читать файл по-строчно
len(text) # Получить длину одной строки
text[100] # Получить значение 100 элемента - "1 строка"
open_file.close()

with open(file_path, 'r') as open_file: # Открыть файл так, чтобы после окончания блока он сам закрылся
    text = open_file.readlines() # Прочесть файл построчно, переменная text не будет уничтожена
text[101] # Получить строку
open_file.closed # True Проверка на закрытость

# open(file_path, 'rb') # b - специальный режим доступа к двоичным файлам чтобы их не повредить
# т.е. - без преобразования символов конца строки

with open('.envrc', 'w') as opened_file: # Открыть файл для записи
    opened_file.write(text) # Записать текст в файл (перезаписать!)

# Функция open создает файл, если он еще не существует, и перезаписывает в противном случае.
# Чтобы сохранить существующее содержимое файла и просто добавить данные в его конец, используйте флаг a.
# Для безопасной записи двоичных данных можно использовать флаг wb или ab.

# pathlib
import pathlib
path = pathlib.Path("bookofdreams.txt")
path.read_text() # Прочесть текст
path.write_text("LOG:DEBUG") # Записать текст
path.read_bytes # Прочесть двоичные данные

# Json
# С Json можно работать при помощи readlines и write а потом разделять на куски при помощи сопоставления
# а можно использовать модуль Json

import json
from pprint import pprint

with open('service-policy.json', 'r') as opened_file:
    policy = json.load(opened_file)

    # {'Statement': {'Action': 'service-prefix:action-name',
    # 'Resource': '*'},
    # 'Version': '2012-10-17'}  

pprint(policy) # Вывести данные json в удобочитаемом формате
policy['Statement']['Resource'] = 'S3' # Изменить значение поля Resource

with open('service-policy.json', 'w') as opened_file: # открыть в режиме записи
    policy = json.dump(policy, opened_file) # Записать изменения в json-файл

# YAML
import yaml # Импортируем пакет
with open('verify-apache.yml', 'r') as opened_file: # Открываем файл в режиме чтения
    verify_apache = yaml.safe_load(opened_file) # Читаем файл

pprint(verify_apache) # Выводим содержимое в удобном виде

with open('verify-apache.yml', 'w') as opened_file: # Открываем файл в режиме записи
    yaml.dump(verify_apache, opened_file) # Записываем информацию

# XML
import xml.etree.ElementTree as ET # Испортируем пакет XML
tree = ET.parse('http_feeds.feedburner.com_oreilly_radar_atom.xml') # Получаем структуру и данные XML

root = tree.getroot() # Находим корень
for child in root: # Запускаем проход по дереву
    print(child.tag, child.attrib) # Печатаем ключ и его значение

ns = {'default':'http://www.w3.org/2005/Atom'} # Передаем словарь с известным значением для поиска
authors = root.findall("default:entry/default:author/default:name", ns) #Ищем все строки по поисковому запросу

for author in authors: # Проходим по строкам
    print(author.text) # Выводим на экран

# CSV

import csv
file_path = 'registered_user_count_ytd.csv'
with open(file_path, newline='') as csv_file:
    off_reader = csv.reader(csv_file, delimiter=',') # Загрузить строки и разбить из на подстроки согласно разделителя
    for _ in range(5):
        print(next(off_reader)) 

# Pandas
#import pandas as pd
#df = pd.read_csv('sample-data.csv') # Загрузить данные в ДатаФрейм из .csv файла
#df.head(3) # Просмотреть несколько первых строк объекта DataFrame
#df.describe() # Просмотреть статистику по ДатаФрейму
#df['close']  # Просмотерть конкретный столбец данных



