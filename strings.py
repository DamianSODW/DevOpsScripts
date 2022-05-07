#Строки
str()
input = "some new string!"
output = 'some new string!'
my_list = list()
str(my_list)
multi_line = """This is a
multi-line string,
which includes linebreaks.
"""
input.strip() # Удалить пробелы в начале и в конце
input.rstrip() # Удалить пробелы в конце
input.lstrip() # Удалить пробелы в начале

output.ljust(1) # Добавить 1 пробел слева
output.rjust(1,"*") # Добавить 1 * справа

# Разбить строку с разделителями (по-умолчанию пробел)
text = "Mary had a little lamb"
text.split() # ['Mary', 'had', 'a', 'little', 'lamb']
url = "gt.motomomo.io/v2/api/asset/143"
url.split('/') # ['gt.motomomo.io', 'v2', 'api', 'asset', '143']

# Вставить разделить между элементами списка
items = ['cow', 'milk', 'bread', 'butter']
" and ".join(items) # 'cow and milk and bread and butter'

name = "bill monroe"
name.capitalize() # 'Bill monroe'
name.upper() # 'BILL MONROE'
name.title() # 'Bill Monroe'
name.swapcase() # 'BILL MONROE'
name = "BILL MONROE"
name.lower() # 'bill monroe'

"William".startswith('W') # True
"Molly".endswith('olly') # True
"abc123".isalnum() # True
"abc123".isalpha() # False
"123".isnumeric() # True
"Sandy".istitle() # True
"Sandy".islower() # False
"SANDY".isupper() # True

# Интерполяция строк с использование метода format
'{} comes before {}'.format('first', 'second') # 'first comes before second'
'{1} comes after {0}, but {1} comes before {2}'.format(
    'first','second','third')
    # 'second comes after first, but second comes before third'

# подстановка по имени параметра
'''{country} is an island.
{country} is off of the coast of
{continent} in the {ocean}'''.format(ocean='Indian Ocean',
                                    continent='Africa',
                                    country='Madagascar')
#'Madagascar is an island.
#Madagascar is off of the coast of
#Africa in the Indian Ocean'

# Подстановка ключей из асоциативного массива
values = {'first': 'Bill', 'last': 'Bailey'}
"Won't you come home {first} {last}?".format(**values)
# "Won't you come home Bill Bailey?"

# Язык форматирования f-строк
a = 1
b = 2
f"a is {a}, b is {b}. Adding them results in {a + b}"
#'a is 1, b is 2. Adding them results in 3'

# спецификации форматирования начинаются с двоеточия
count = 43
f"|{count:5d}" # '   |43'
padding = 10
f"|{count:{padding}d}" # '         |43' 
  # Спец. форм могут получать значения из переменных, например число пробелов

# Шаблонизированные строки

from string import Template # Импортировать функционал

greeting = Template("$hello Mark Anthony") # Создать шаблон с параметром $hello
greeting.substitute(hello="Bonjour") # 'Bonjour Mark Anthony'
