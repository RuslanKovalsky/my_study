"""class Contact:
    def __init__(self, name, phone, address, birthday):
        self.name = name
        self.phone = phone
        self.address = address
        self.birthday = birthday
        # добавьте свойство address
        # добавьте свойство birthday
        print(f"Создаём новый контакт {name}")


# здесь создайте объекты mike и vlad
mike = Contact('Михаил Булгаков', '2-03-27', 'Россия, Москва, Большая Пироговская, дом 35б, кв. 6', '15.05.1891')
vlad = Contact('Владимир Маяковский', '73-88', 'Россия, Москва, Лубянский проезд, д. 3, кв. 12', '19.07.1893')
def print_contact():
    print(f"{mike.name} — адрес: {mike.address}, телефон: {mike.phone}, день рождения: {mike.birthday}")
    print(f"{vlad.name} — адрес: {vlad.address}, телефон: {vlad.phone}, день рождения: {vlad.birthday}")
print_contact()
# здесь вызовите функцию print_contact(),
# и она напечатает на экране данные контактов mike и vlad"""


"""class Contact:
    def __init__(self, name, phone, birthday, address):
        self.name = name
        self.phone = phone
        self.birthday = birthday
        self.address = address
        print(f"Создаём новый контакт {name}")


mike = Contact("Михаил Булгаков", "2-03-27", "15.05.1891", "Россия, Москва, Большая Пироговская, дом 35б, кв. 6")
vlad = Contact("Владимир Маяковский", "73-88", "19.07.1893", "Россия, Москва, Лубянский проезд, д. 3, кв. 12")


def print_contact():
    print(f"{mike.name} — адрес: {mike.address}, телефон: {mike.phone}, день рождения: {mike.birthday}")
    print(f"{vlad.name} — адрес: {vlad.address}, телефон: {vlad.phone}, день рождения: {vlad.birthday}")


# здесь измените адрес для объекта mike
# здесь измените телефон для объекта mike
mike.phone = 'К-058-67'
mike.address = 'Россия, Москва, Нащокинский переулок, дом 3, кв. 44'
# здесь измените адрес для объекта vlad
# здесь измените телефон для объекта vlad
vlad.phone = '2-35-71'
vlad.address = 'Россия, Москва, Гендриков переулок, дом 15, кв. 5'

print_contact()  # выводим данные на экран"""



#Задача №3
"""class Contact:
    def __init__(self, name, phone, birthday, address):
        self.name = name
        self.phone = phone
        self.birthday = birthday
        self.address = address
        print(f"Создаём новый контакт {name}")
    # здесь напишите метод show_contact()
    # он будет очень похож на функцию print_contact()

    def show_contact(self):
        print (f"{self.name} — адрес: {self.address}, телефон: {self.phone}, день рождения: {self.birthday}")


    def __str__(self):
        return(f"{self.name} — адрес: {self.address}, телефон: {self.phone}, день рождения: {self.birthday}")


mike = Contact("Михаил Булгаков", "2-03-27", "15.05.1891", "Россия, Москва, Большая Пироговская, дом 35б, кв. 6")
vlad = Contact("Владимир Маяковский", "73-88", "19.07.1893", "Россия, Москва, Лубянский проезд, д. 3, кв. 12")

print(mike)
print(vlad)"""
"""1.
В прошлом задании для вывода на экран данных о каждом объекте мы писали отдельный код для каждого объекта.
 Это громоздко и нерационально, ООП позволяет оптимизировать код.
 
В классе Contact создайте метод show_contact(), который будет выводить данные любого объекта типа Contact в 
том же виде, как сейчас их выводит функция print_contact.
В теле класса Contact напишите метод show_contact, который в качестве параметра будет принимать переменную 
self. В теле метода выполните print(), точно такой же, как в функции print_contact, только вместо имени 
объекта в аргументе укажите self.
Вызовите метод show_contact для объектов mike и vlad
Удалите из кода функцию print_contact().
Запустите код"""


"""
В прекоде подготовлен класс Planet, он описывает планеты и хранит свойства: name (имя), surface_area 
(площадь поверхности в км²), average_temp_celcius (средняя температура поверхности планеты по Цельсию),
 average_temp_fahrenheit (то же по Фаренгейту).
Конструктор класса принимает на вход три параметра: имя планеты, её радиус в километрах и среднюю температуру 
на поверхности в градусах Цельсия.
В конструкторе вычислите площадь поверхности планеты. Для упрощения считайте планеты сферическими.
Площадь поверхности сферы с радиусом r равна 4 * π * r² . Значение числа π получите так: math.pi (для этого 
подключите модуль math).
В конструкторе вычислите температуру поверхности по Фаренгейту.
Чтобы перевести температуру по Цельсию в ш
калу Фаренгейта, нужно умножить значение на 9/5 и прибавить 32."""

# импортируйте библиотеку math
"""import math


class Planet:
    def __init__(self, name, radius, temp_celsius):
        self.name = name
        self.surface_area = 4 * math.pi * radius * radius
        self.average_temp_celsius = temp_celsius
        self.average_temp_fahrenheit = (9 / 5) * temp_celsius + 32

    def show_info(self):
        print(f"Планета {self.name} имеет площадь поверхности {self.surface_area} кв.км.")
        print(f"Средняя температура поверхности планеты: {self.average_temp_fahrenheit} по Фаренгейту.")

    #def __str__(self):
     #   return (f"Планета {self.name} имеет площадь поверхности {self.surface_area} кв.км. Средняя температура поверхности планеты: {self.average_temp_fahrenheit} по Фаренгейту.")
# этот вариант тоже рабочий.

jupiter = Planet('Юпитер', 69911, -108)
# вызовите метод show_info для Юпитера
jupiter.show_info()"""

"""class Bird:
    #  Это конструктор, он вызывается при создании объекта
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def show(self):
        # Вызывается для вывода на экран всех свойств объекта
        # это интерфейс класса, к нему можно обратиться из внешнего кода
        print(f'{self.name} носит одежду размера "{self.size}".')


# Создание объекта
sparrow = Bird('Воробей', 'S')
# Теперь можно воспользоваться его внешним интерфейсом: методом show()
sparrow.show()

# Результат: Воробей носит одежду размера "S"."""

"""class Bird:
    def __init__(self, name, size):
        # Это конструктор, он вызывается при создании объекта
        self.name = name
        self.size = size

    def show(self):
        # Вызывается для вывода на экран всех свойств объекта
        print(f'{self.name} носит одежду размера {self.size}.')


class Parrot(Bird):
    def __init__(self, name, size, sound):
        super().__init__(name, size)
        self.sound = sound

    def show(self):
        # Вызывается для вывода на экран всех свойств объекта
        print(f'{self.name} носит одежду размера {self.size} и {self.sound}.')


# Создание объектов
sparrow = Bird('Воробей', 'S')
ara = Parrot('Попугай ара', 'XL', 'разговаривает')
nymphicus = Parrot('Попугай Корелла', 'S', 'щебечет')

# Теперь можно воспользоваться его внешним интерфейсом: методом show()
sparrow.show()
ara.show()
nymphicus.show()"""

# Результат:
# Воробей носит одежду размера S.
# Попугай ара носит одежду размера XL и разговаривает.
# Попугай Корелла носит одежду размера S и щебечет.

"""class Bird:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def show(self):
        print(f'{self.name} носит одежду размера {self.size}.') # это интерфейс


class Parrot(Bird):
    def __init__(self, name, size, sound): # здесь наследуем от класса Bird
        super().__init__(name, size) # супером оставляем name , size
        self.sound = sound # добавляем новый параметр

    def show(self):  # это интерфейс
        print(f'{self.name} носит одежду размера {self.size} и {self.sound}.')


class Predator(Bird): # здесь наследуем от класса Bird
    def __init__(self, name, size, claws_size):
        super().__init__(name, size)
        self.claws_size = claws_size

    def show(self):
        print(f'{self.name} носит одежду размера {self.size} и '
              f'когти размера {self.claws_size}.')


class Egg(Predator):
    def show(self):
        print(f'Из яйца вылупится птичка {self.name} размера {self.size} с '
              f'когтями размера {self.claws_size}.')"""


# импортируем функции из библиотеки math для рассчёта расстояния
"""from math import radians, sin, cos, acos


class Point:
    def __init__(self, latitude, longitude):
        self.latitude = radians(latitude)
        self.longitude = radians(longitude)

    # считаем расстояние между двумя точками в км
    def distance(self, other):
        cos_d = sin(self.latitude) * sin(other.latitude) + cos(self.latitude) * cos(other.latitude) * cos(
        self.longitude - other.longitude)

        return 6371 * acos(cos_d)


class City(Point):
    def __init__(self, latitude, longitude, name, population):
        # допишите код: сохраните свойства родителя
        # и добавьте свойства name и population
        super().__init__(latitude, longitude)
        self.name = name
        self.population = population

    def show(self):
        print(f"Город {self.name}, население {self.population} чел.")


class Mountain(Point):
    # допишите код: напишите конструктор, в нём сохраните свойства родителя
    # и добавьте свойства name и height
    def __init__(self, latitude, longitude, name, height):
        super().__init__(latitude, longitude)
        self.name = name
        self.height = height
    # Создайте метод show(self):
    def show(self):
        print(f'Высота горы {self.name} - {self.height} м.')
    # информацию о горе нужно вывести в формате:
    # "Высота горы <название> - <высота> м."


# эта функция печатает расстояние
# между двумя любыми наследниками класса Point
def print_how_far(geo_object_1, geo_object_2):
    print(f'От точки «{geo_object_1.name}» до точки «{geo_object_2.name}» — {geo_object_1.distance(geo_object_2)} км.')


# основной код
moscow = City(55.7522200, 37.6155600, 'Москва', 12615882)
everest = Mountain(27.98791, 86.92529, 'Эверест', 8848)
chelyabinsk = City(55.154, 61.4291, 'Челябинск', 1200703)

moscow.show()
everest.show()
print_how_far(moscow, everest)
print_how_far(moscow, chelyabinsk)"""

"""Опишите на ООП взаимодействие студента, ментора, код-ревьюера и куратора.
Все эти люди — люди, поэтому создадим базовый класс Human, со свойством name (у каждого человека 
должно быть имя) и методом answer_question() для ответов на вопросы.

По умолчанию объект Human будет отвечать на любой вопрос так: «Очень интересный вопрос! Не знаю.»
От класса Human унаследуем классы Student, Mentor, CodeReviewer и Curator.
Student должен уметь задавать вопросы. Реализуйте в классе Student метод ask_question(Human, question). 

При вызове этот метод должен:
Напечатать на экране вопрос в формате <имя человека, которому задаём вопрос>, <текст вопроса>
Задать вопрос question человеку, объекту класса Human. Имя объекта, которому адресован вопрос, передаётся 
при вызове метода ask_question().

Объекты классов Mentor, CodeReviewer и Curator должны уметь отвечать на вопросы при вызове метода 
answer_question(). Задан непредусмотренный вопрос — для него подойдет ответ по умолчанию.
После того, как вы допишете код, ваша программа должна вывести на экран такой текст:"""


class Human:
    def __init__(self, name):
        self.name = name

    # ответ по умолчанию для всех одинаковый, можно
    # доверить его родительскому классу
    def answer_question(self, question):
        print('Очень интересный вопрос! Не знаю.')


class Student(Human):
    #  метод ask_question() принимает параметр someone:
    #  это объект, экземпляр класса Curator, Mentor или CodeReviewer,
    #  которому Student задаёт вопрос;
    #  параметр question — это просто строка
    #  имя объекта и текст вопроса задаются при вызове метода ask_question
    def ask_question(self, someone, question):
        # напечатайте на экран вопрос в нужном формате
        super().answer_question(question)
        self.someone = someone
        self.question = question
        print(f'{self.someone}, {self.question}')
        # запросите ответ на вопрос у someone

        print()  # этот print выводит разделительную пустую строку


class Curator(Human):
    def answer_question(self, question):
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        # если да - ответить на него
        # если нет - вызвать метод answer_question() у родительского класса
        if question == 'Марина, мне грустненько, что делать?':
            print('Держись, всё получится. Хочешь видео с котиками?')
        else:
            super().answer_question(question)
# объявите и реализуйте классы CodeReviewer и Mentor
class CodeReviewer(Human):
    def answer_question(self, question):
        if question == 'Евгений, что не так с моим проектом?':
            print('О, вопрос про проект, это я люблю.')
        else:
            super().answer_question(question)

class Mentor(Human):
    def answer_question(self, question):
        if question == 'Ира, мне грустненько, что делать?':
            print('Отдохни и возвращайся с вопросами по теории.')
        elif question == 'Виталя, как устроиться на работу питонистом?':
            print('Очень интересный вопрос! Не знаю.')
        else:
            super().answer_question(question)

# следующий код менять не нужно, он работает, мы проверяли
student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')