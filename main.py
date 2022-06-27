"""a = 16 * 2.2 + 7 - 0.2
print(a)


snake = '38.2'
length = 6.5

result = float(snake) * length

print('В вагоне можно поставить в ряд', int(result), 'попугаев')"""
from itertools import count

"""countdown_str = ''

for i in reversed(range(0, 11)):
    countdown_str = countdown_str + str(i) + ', '

countdown_str = countdown_str + ' поехали!'

print(countdown_str)"""

"""for messages_count in range(0, 21):
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif messages_count == 1:
        print('У вас 1 новое сообщение')
    elif messages_count <= 4:
        print('У вас', messages_count, 'новых сообщения')
    else:
        print('У вас', messages_count, 'новых сообщений')"""


"""for current_hour in range(0, 24):
    print("На часах " + str(current_hour) + ":00.")
    # Вместо многоточий напишите код
    if current_hour < 6:
        print('Доброй ночи!')
    elif current_hour <= 11:
        print('Доброе утро!')
    elif current_hour <= 17:
        print('Добрый день!')
    elif current_hour <= 22:
        print('Добрый вечер!')
    else:
        print('Доброй ночи!')"""


""""# Добавьте новые условия в elif и else
for messages_count in range(0, 21):
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif messages_count == 1:
        # напишите ваш код здесь
        print('У вас 1 новое сообщение')
    elif messages_count <=4:
        # напишите ваш код здесь
        print('У вас ' + str(messages_count) + ' новых сообщения')
    else:
        print('У вас ' + str(messages_count) + ' новых сообщений')"""

"""for messages_count in range(0, 21):
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif messages_count == 1:
        # напишите ваш код здесь
        print('У вас 1 новое сообщение')
    elif messages_count == 2 and 3:
        # напишите ваш код здесь
        print('У вас ' + str(messages_count) + ' новых сообщения')
    elif messages_count == 4 and 5:
        print('У вас ' + str(messages_count) + ' новых сообщения')
    else:
        print('У вас ' + str(messages_count) + ' новых сообщений')"""



"""friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']

# Объявлен пустой словарь, его нужно будет наполнить элементами,
# каждый из которых составлен по схеме "имя: город"
friends =  {}

# Допишите ваш код сюда
for i in range(0, len(friends_names)):
    friends[friends_names[i]] = friends_cities[i]

#print("Лена живёт в городе",'Москва' )

a = input('Введите имя ')
a = str(a)
name = a

if name in friends:
    print(name + ' живёт в городе ' + friends[name])
    
    
favorite_songs = {
    'Серёга': ['Unforgiven', 'Holiday', 'Highway to hell'], 
    'Соня': ['Shake it out', 'The Show Must Go On', 'Наше лето'], 
    'Дима': ['Владимирский централ', 'Мурка', 'Третье сентября',]
}
# Ниже напишите код, который напечатает на экран, сколько у Димы любимых песен

# Ниже напишите код, который построчно напечатает
# все любимые песни Сони.
dima = len(favorite_songs['Дима'])
print(dima)
sonya = favorite_songs['Соня']
for sonya in favorite_songs['Соня']:
    print(sonya)"""

"""friends = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Хабаровск',
    'Егор': 'Пермь'
}


def is_anyone_in(collection, city):
    for friend in friends:
        if collection[friend] == city:
            print('В городе ' + collection[friend] + ' живёт ' + friend + '.' + ' Обязательно зайду в гости!')
        else:
            print('В городе ' + collection[friend] + ' у меня есть друг, но мне туда не надо.')


is_anyone_in(friends, 'Хабаровск')"""

"""milk_str = 'молоковоз'

# Применяем метод split() с аргументом 'о':
new_list = milk_str.split('о')

print(new_list)
# Будет напечатано: ['м', 'л', 'к', 'в', 'з']"""


"""counter_str = 'Раз-два-три-четыре-пять, вышел зайчик погулять'

# Преобразуем строку в список, а разделителем будет дефис
counter_list = counter_str.split('-')
print(counter_list)

# Создадим ещё одну строку
blok_str = 'Ночь. Улица. Фонарь. Аптека'
# Разобьём фразу по словам.
# Разделителем будет служить сочетание точки и пробела:
blok_list = blok_str.split('. ')
print(blok_list)"""

"""message = 'У меня опять всё сломалось и не работает соединение с интернетом!!11 Нужна стоимость работ'

# Разбиваем сообщение по пробелам на слова
words = message.split()
# Проверяем, есть ли ключевые слова в письме
if 'стоимость' in words:
    print('Переслать письмо в отдел биллинга')
elif 'сломалось' in words:
    print('Переслать письмо в техподдержку')
elif 'сломалось' and 'стоимость' in words:
    print('Читаем сами')
else:
    print('Содержание письма не определено, придётся прочесть самостоятельно')"""

"""quote_1 = 'Работает? Не трогай'
quote_2 = 'Если твой код работает, значит это хороший код'
quote_3 = 'Лень - главное достоинство программиста'

def penult_word(message):
    word_list = message.split()
    return word_list[-3]

# Вызовы функции готовы к работе, не изменяйте их!

# Вызываем функцию penult_word с аргументом quote_1 и печатаем результат её работы.
print(penult_word(quote_1))

# То же, но с аргументом quote_2.
print(penult_word(quote_2))

# То же с аргументом quote_3.
print(penult_word(quote_3))"""

"""import datetime as dt

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2
}
Получите текущее время UTC: вызовите метод dt.datetime.utcnow().
Преобразуйте поправку к UTC города в timedelta: dt.timedelta(hours = UTC_OFFSET[city])
Получите местное время: к текущему времени UTC прибавьте timedelta.
Верните из функции получившееся значение с помощью команды return


def what_time(city):
    # Напишите код тела функции;
    # она должна вернуть текущее время в городе city

    utc_time = dt.datetime.utcnow()
    period = dt.timedelta(hours = UTC_OFFSET[city])
    what_time = utc_time + period
    return what_time

print(what_time('Екатеринбург'))"""


import datetime as dt

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь'
}

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2
}

"""def what_time(friend):
    # напишите код тела функции
    # пусть она вернет время у друга из аргумента friend
    utc_time = dt.datetime.utcnow()
    city = DATABASE[friend]
    period = dt.timedelta(hours = UTC_OFFSET[city])
    what_time = utc_time + period
    return what_time
def what_friend(friend):
    names = DATABASE.keys()
print(names)


#print(f'В городе где живет {name} время равно: ')
print(what_time('Соня'))"""


"""import datetime as dt

arrival_time = dt.datetime(2019, 5, 10, 19, 45)

print('Самолёт прибывает в', arrival_time)
print('Самолёт прибывает в', arrival_time.strftime('%H:%M'))

first_snow = dt.datetime(2018, 9, 9)

# дата последнего весеннего снега в Новосибирске в 2018
last_snow = dt.datetime(2018, 5, 19)

print(last_snow.strftime('Последний снег выпал в %U-ю неделю года.'))
print(first_snow.strftime('А первый снег пошёл в %U-ю неделю.')) """


"""import datetime as dt


DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь'
}

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 4,
    'Краснодар': 3,
    'Калининград': 2
}


def what_time(friend):
    utc_time = dt.datetime.utcnow()
    city = DATABASE[friend]
    what_time = utc_time + dt.timedelta(hours=UTC_OFFSET[city])
    return what_time.strftime('%H:%M')



print(what_time('Соня'))"""

"""import datetime as dt

DATABASE = {
    'Сергей': 'Омск',
    'Соня': 'Москва',
    'Алексей': 'Калининград',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск',
    'Артём': 'Владивосток',
    'Петя': 'Михайловка'
}

UTC_OFFSET = {
    'Москва': 3,
    'Санкт-Петербург': 3,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Самара': 4,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Воронеж': 3,
    'Пермь': 5,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2,
    'Владивосток': 10
}


def format_count_friends(count_friends):
    if count_friends == 1:
        return '1 друг'
    elif 2 <= count_friends <= 4:
        return f'{count_friends} друга'
    else:
        return f'{count_friends} друзей'


def what_time(city):
    offset = UTC_OFFSET[city]
    city_time = dt.datetime.utcnow() + dt.timedelta(hours=offset)
    f_time = city_time.strftime("%H:%M")
    return f_time


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(DATABASE)
        return f'У тебя {format_count_friends(count)}.'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


def process_friend(name, query):
    if name in DATABASE:
        city = DATABASE[name]
        if query == 'ты где?':
            return f'{name} в городе {city}'
        elif query == 'который час?':
            if city in UTC_OFFSET:
                return f'Там сейчас {what_time(city)}'
            else:                                             #сюда он похоже не заходит так как условие if выполнилось
                return f'<не могу определить время в городе {city}>'# эта строчка не работает, вопрос почему?....

        else:
            return '<неизвестный запрос>'
    else:
        return f'У тебя нет друга по имени {name}'



def process_query(query):
    elements = query.split(', ')
    if elements[0] == 'Анфиса':
        return process_anfisa(elements[1])
    else:
        return process_friend(elements[0], elements[1])


def runner():
    queries = [
        'Анфиса, сколько у меня друзей?',
        'Анфиса, кто все мои друзья?',
        'Анфиса, где все мои друзья?',
        'Анфиса, кто виноват?',
        'Коля, ты где?',
        'Соня, что делать?',
        'Антон, ты где?',
        'Алексей, который час?',
        'Артём, который час?',
        'Антон, который час?',
        'Петя, который час?'
    ]
    for query in queries:
        print(query, '-', process_query(query))

runner()"""

"""import urllib.parse


url = 'https://yandex.ru/search/?text=%D0%BA%D0%B0%D0%BA%20%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0%BE%20%D0%B5%D0%B7%D0%B4%D0%B8%D1%82%D1%8C%20%D0%BD%D0%B0%20%D1%82%D0%B0%D0%BA%D1%81%D0%B8'

# чтобы вычленить текст вопроса
# разбейте строку по знаку = и возьмите
# второй элемент получившегося списка

question = url.split('=')[1]



# сохраните его в переменной question

# напечатайте на экран запрос в расшифрованном виде
print(urllib.parse.unquote(question))  # ваш код здесь"""

"""import requests

url = 'http://wttr.in/?0T'

response = requests.get(url)  # выполните HTTP-запрос

print(response.text)  # напечатайте текст HTTP-ответа"""


"""import requests


url = 'https://wttr.in'  # не изменяйте значение URL

weather_parameters = {
    '0': '', 'T': '', 'M': '', 'lang': 'ru'
    # добавьте параметр запроса `T`, чтобы вернулся чёрно-белый текст
}
params = weather_parameters
response = requests.get((url), (params))   # передайте параметры в http-запрос

print(response.text)

import requests

url = 'https://wttr.in'

weather_parameters = {
    '0': '',
    'T': '',
   # удалите этот параметр
    'M': ''
}
params = weather_parameters
request_headers = {'Accept-Language': 'ru'
    # заполните словарь с заголовками
}

# не забудьте передать параметры и заголовки в http-запрос
# через аргументы `params` и `headers` функции get()
response = requests.get(url, params=weather_parameters, headers=request_headers)
print(response.text)"""

dump = {
    1: 'единица',               # Ключ - число, значение - строка.
    'земляника': 'ягода',       # И ключ, и значение - строки.
    'помидор': 'ягода',         # Значение 'ягода' - не уникально. Так можно.
    False: 0,                   # Ключ - булево значение, значение - число.
    'лук': ['овощ', 'оружие'],  # Ключ - строка, значение - список.
                                # Ключ - строка, а значение - словарь. Так тоже можно!
    'англо-русский словарь': {'рука': 'hand',
                              'нога': 'leg',
                              'бэкенд-разработчик': 'back-end developer'
                               },
}

print(dump['англо-русский словарь'])
