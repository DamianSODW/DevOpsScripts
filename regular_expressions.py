import re # Импортируем пакет с регулярными выражениями

cc_list = '''Ezra Koenig <ekoenig@vpwk.com>,
Rostam Batmanglij <rostam@vpwk.com>,
Chris Tomson <ctomson@vpwk.com,
Bobbi Baio <bbaio@vpwk.com'''

'Rostam' in cc_list # Поиск по тексту
re.search(r'Rostam', cc_list) # Альтернативный поиск по тексту
re.search(r'[RB]obb[iy]', cc_list) # В [] указываюется варианты символов
re.search(r'Chr[a-z][a-z]', cc_list) # Можно использовать дапазоны A-Z, 0-9
re.search(r'[A-Za-z]+', cc_list) # Ezra Символ + после элемента соответствует одному или нескольким экземплярам
re.search(r'[A-Za-z]{6}', cc_list) # Koenig В {} указывается число повторений
# Символ « . » — джокерный, он соответствует произвольному символу.
# Для поиска настоящего символа « . » нужно его экранировать \
re.search(r'[A-Za-z]+@[a-z]+\.[a-z]+', cc_list) # Поиск адреса эл. почты
# Существуют готовые символы \w, эквивалентный [a-zA-Z0-9_], и \d , эквивалентный [0-9].
re.search(r'\w+', cc_list) # Ezra
re.search(r'\w+\@\w+\.\w+', cc_list) # Альтернативный вариант с эл. почтой

# Группы
matched = re.search(r'(\w+)\@(\w+)\.(\w+)', cc_list)
matched.group(0) # 'ekoenig@vpwk.com'
matched.group(1) # 'ekoenig'
matched.group(2) # 'vpwk'
matched.group(3) # 'com'
# Именованные группы - ?P<Название>
matched = re.search(r'(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)', cc_list)
matched.group('name') # 'ekoenig'

# Найти все
matched = re.findall(r'\w+\@\w+\.\w+', cc_list)
#['ekoenig@vpwk.com', 'rostam@vpwk.com', 'ctomson@vpwk.com', 'cbaio@vpwk.com']

matched = re.findall(r'(\w+)\@(\w+)\.(\w+)', cc_list)
#[('ekoenig', 'vpwk', 'com'), ('rostam', 'vpwk', 'com'),
#('ctomson', 'vpwk', 'com'), ('cbaio', 'vpwk', 'com')]
names = [x[0] for x in matched]
# ['ekoenig', 'rostam', 'ctomson', 'cbaio']

# Поисковый итератор finditer - Next
matched = re.finditer(r'\w+\@\w+\.\w+', cc_list) # Получить итератор
next(matched) # Получить первое вхождение подстроки
next(matched) # Получить второе вхождение подстроки

# Перебор в цикле
matched = re.finditer("(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)", cc_list)
for m in matched:
    print(m.groupdict()) # {'name': 'ekoenig', 'SLD': 'vpwk', 'TLD': 'com'}

# Подстановка
re.sub("\d", "#", "The passcode you entered was 09876") # Заменить все символы от 0-9 на #
# 'The passcode you entered was #####'
users = re.sub("(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)", "\g<TLD>.\g<SLD>.\g<name>", cc_list)
"""Ezra Koenig <com.vpwk.ekoenig>,
Rostam Batmanglij <com.vpwk.rostam>,
Chris Tomson <com.vpwk.ctomson,
Chris Baio <com.vpwk.cbaio"""

# Компиляция
regex = re.compile(r'\w+\@\w+\.\w+') # Скомпилировать рег. выржаение для ускорения его работы
regex.search(cc_list) # ekoenig@vpwk.com

# Поиск в тексте с помощью регулярных выражений
# Единый формат журналов (Common Log Format, CLF)
# <IP-адрес> <Id клиента> <Id пользователя> <Время> <Запрос> <Состояние> <Размер>
# 127.0.0.1 - swills [13/Nov/2019:14:43:30 -0800] "GET /assets/234 HTTP/1.0" 200 2326

line = '127.0.0.1 - rj [13/Nov/2019:14:43:30-0000] "GET HTTP/1.0" 200'
m = re.search(r'(?P<IP>\d+\.\d+\.\d+\.\d+)', line) # Получить IP-адрес
m.group('IP') # 127.0.0.1

r = r'\[(?P<Time>\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})\]' # Получить дату и время
m = re.search(r, line)
m.group('Time')

# Регулярное выражение по частям
r = r'(?P<IP>\d+\.\d+\.\d+\.\d+)'
r += r' - (?P<User>\w+) '
r += r'\[(?P<Time>\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})\]'
r += r' (?P<Request>".+")'
m = re.search(r, line)
m.group('IP') # '127.0.0.1'
m.group('User') # 'rj'
m.group('Time') # '13/Nov/2019:14:43:30'
m.group('Request') # '"GET HTTP/1.0"'

# Выборка из всего журнала за кокретную дату
access_log = cc_list
r = r'(?P<IP>\d+\.\d+\.\d+\.\d+)'
r += r'- (?P<User>\w+)'
r += r'\[(?P<Time>08/Nov/\d{4}:\d{2}:\d{2}:\d{2} [-+]\d{4})\]'
r += r' (?P<Request>"GET .+")'
matched = re.finditer(r, access_log)
for m in matched:
    print(m.group('IP'))

