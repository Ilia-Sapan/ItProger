# 14.1 Klassen und Objekte

# class Klassenname:
#     Docstring
#     def __init__(self, ...):
#         Anweisungen zur Initializierung
#
#     def methode_1(self, ...):
#         Anweisungen

class Flasche: # 1 Kopfzeile der Klassendefinition
    'Modell eine Flasche' # 2 Docstring
    def __init__(self): # 3 Initialisierungmethode, die aufgerufen wird, wenn die Klasse augerufen und ein neues Objekt erzeugt wird
        self.inhalt  = 0 # 4 Das Attribut inhalt wird definiert, und erhält den Anfangswert 0
        self.max_inhalt = 1000
        self.geöffnet = False
    def öffnen(self):
        self.geöffnet = True # 5 Das Attribut geöffnet erhält den Wert True. Die Flasche ist jetzt geöffnet
    def schließen(self):
        self.geöffnet = False
    def füllen(self, volumen):
        if self.geöffnet: # 6 Nur wenn die Flasche geöffnet ist, kann sie befüllt werden
            if self.inhalt + volumen <= self.max_inhalt:
                self.inhalt += volumen # 7 Wenn das Volumen volumen noch in die Flasche passt, wird es dem inhalt hinzugefügt. Das Attribut inhalt bekommt dann einen neuen Wert.
    def leeren(self):
        if self.geöffnet:
            self.inhalt = 0 # 8 Die Methode leeren() ist so definiert, dass die Flasche sich vollständig entleert

a = Flasche()
# object.attribut
# print(a.max_inhalt)
# a.öffnen()
# a.füllen(100)
# print(a.inhalt)
a.füllen(500)
print(a.inhalt)
b = Flasche()
b.öffnen()
b.füllen(500)
b.füllen(1000)
print(b.inhalt) # Выдаст 500, т.к. бутылка переполнена на 500

# Objekte mit variablen Anfangswerten

# def __init__(self, fassungsvermögen):
#     self.inhalt = 0
#     self.max_inhalt = fassungsvermögen
#     self.geöffnet = False
# kleine_flasche = Flasche(200)

class Geld:  # Создание класса "Geld" для представления денег.

    wechselkurs = {'USD': 0.8154,  # Курс обмена для разных валют относительно евро.
                   'GBP': 1.1129,
                   'EUR': 1.0,
                   'JPY': 0.0079}

    def __init__(self, währung, betrag):  # Конструктор класса, который инициализирует валюту и сумму.
        self.währung = währung  # Присваиваем валюту (например, 'USD', 'EUR' и т.д.).
        self.betrag = betrag  # Присваиваем сумму в указанной валюте.

    def berechneEuro(self):  # Метод для вычисления эквивалента суммы в евро.
        return self.betrag * self.wechselkurs[self.währung]  # Возвращаем сумму в евро, умножив на курс валюты.

    def add(self, geld):  # Метод для добавления двух объектов Geld (денег).
        a = self.berechneEuro()  # Преобразуем текущую сумму в евро.
        b = geld.berechneEuro()  # Преобразуем сумму из другого объекта Geld в евро.
        summe = (a + b) / self.wechselkurs[self.währung]  # Складываем суммы в евро и возвращаем в исходную валюту.
        return Geld(self.währung, summe)  # Возвращаем новый объект Geld с суммой в исходной валюте.

a = Geld('EUR', 12)
print(a) # <__main__.Geld object at 0x0000018F4C368950>
print(a.währung, a.betrag)
b = a.add(Geld('USD',1))
print(b.währung,b.betrag)

# Klasseatribute

# klassenatribut = wert
# klasse.klassenatribut


print(Geld.wechselkurs) # {'USD': 0.8154, 'GBP': 1.1129, 'EUR': 1.0, 'JPY': 0.0079}

# Operatoren überladen – Polymorphie

a = 10
# a + 3 # 13
print(a.__add__(2))


class Geld:  # Создаём класс "Geld", который моделирует денежные суммы в разных валютах.
    'Die Klasse modelliert Geldbeträge'  # Докстринг: Класс моделирует денежные суммы.

    wechselkurs = {'USD': 0.8154,  # Словарь обменных курсов для разных валют относительно евро.
                   'GBP': 1.1129,
                   'EUR': 1.0,
                   'JPY': 0.0079}  # Курс обмена для евро и других валют.

    def __init__(self, währung, betrag):  # Конструктор класса, инициализирует валюту и сумму.
        self.währung = währung  # Устанавливаем валюту (например, 'USD', 'EUR').
        self.betrag = float(betrag)  # Устанавливаем сумму, преобразуя её в число с плавающей точкой (для точности).

    def berechneEuro(self):  # Метод для вычисления эквивалента суммы в евро.
        return self.betrag * self.wechselkurs[self.währung]  # Возвращаем сумму в евро, умножив на курс валюты.

    def __add__(self, geld):  # Метод для сложения двух объектов класса Geld.
        a = self.berechneEuro()  # Преобразуем текущую сумму в евро.
        b = geld.berechneEuro()  # Преобразуем сумму другого объекта Geld в евро.
        summe = (a + b) / self.wechselkurs[self.währung]  # Складываем суммы в евро и возвращаем в исходную валюту.
        return Geld(self.währung, summe)  # Возвращаем новый объект Geld с результатом сложения в исходной валюте.

    def __str__(self):  # Метод для строкового представления объекта.
        return "{} {}".format(self.währung, round(self.betrag,
                                                  2))  # Возвращаем строку вида "валюта сумма", с округлением до 2 знаков.


if __name__ == '__main__':  # Это проверка, чтобы код выполнялся только при прямом запуске скрипта, а не при его импорте.
    a = Geld('EUR', 10)  # Создаём объект a с валютой EUR и суммой 10.
    b = Geld('USD', 1)  # Создаём объект b с валютой USD и суммой 1.
    print(a + b)  # Складываем объекты a и b, используя перегрузку оператора +, и выводим результат.

# Magische Methods
#
# __init__(self, ...)
# Конструктор класса, вызывается при создании объекта. Используется для инициализации атрибутов объекта.
#
# __str__(self)
# Возвращает строковое представление объекта, используется функцией print() и str() для вывода объекта в удобочитаемом виде.
#
# __repr__(self)
# Возвращает строковое представление объекта, которое предназначено для разработчиков (например, для использования в интерпретаторе). Рекомендуется, чтобы результат был валидным кодом Python.
#
# __add__(self, other)
# Перегружает оператор + для объектов класса. Определяет, как складывать два объекта.
#
# __sub__(self, other)
# Перегружает оператор -. Определяет, как вычитаются два объекта.
#
# __mul__(self, other)
# Перегружает оператор *. Определяет, как умножаются два объекта.
#
# __getitem__(self, key)
# Позволяет использовать объекты класса как коллекции (например, с использованием индекса). Это позволяет обращаться к элементам объекта как к элементам списка или словаря.
#
# __setitem__(self, key, value)
# Позволяет устанавливать значения в объекте, используя синтаксис индексации (например, obj[key] = value).
#
# __delitem__(self, key)
# Перегружает операцию удаления элемента из объекта, используя синтаксис del obj[key].
#
# __len__(self)
# Определяет поведение функции len() для объекта. Этот метод должен возвращать целое число, показывающее длину объекта (например, количество элементов в объекте).

# 14.5 Vererbung

