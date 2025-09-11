class Auto:
    def __init__(self, marke, model, kilometerstand, tankfuehlung):
        self.marke = marke  # Марка автомобиля
        self.model = model  # Модель автомобиля
        self.kilometerstand = kilometerstand  # Пробег автомобиля
        self.tankfuehlung = tankfuehlung  # Уровень топлива в процентах

    def fahren(self, kilometers):
        # Увеличиваем пробег на пройденные километры
        self.kilometerstand += kilometers

        # Рассчитываем расход топлива: 5% на 100 км
        verbrauch = 0.05 * self.tankfuehlung * (kilometers / 100)

        # Уменьшаем уровень топлива
        self.tankfuehlung -= verbrauch

        # Если топливо закончилось, устанавливаем уровень топлива в 0
        if self.tankfuehlung < 0:
            self.tankfuehlung = 0

        # Выводим результат
        print(f"Gefahrene Kilometer: {kilometers}. Verbleibende Tankfüllung: {self.tankfuehlung:.2f}%.")




    def tanken(self, prozent):
        if 0 <= self.tankfuehlung < 100:
            self.tankfuehlung += (0.01*prozent)*self.tankfuehlung
            print(f"Verbleibende Tankfüllung: {self.tankfuehlung:.2f}%.")

mein_auto = Auto("Volkswagen", "Golf", 50000, 50)
mein_auto.fahren(100)
mein_auto.fahren(300)
mein_auto.tanken(12)




# class Flasche: # 1 Kopfzeile der Klassendefinition
#     'Modell eine Flasche' # 2 Docstring
#     def __init__(self): # 3 Initialisierungmethode, die aufgerufen wird, wenn die Klasse augerufen und ein neues Objekt erzeugt wird
#         self.inhalt  = 0 # 4 Das Attribut inhalt wird definiert, und erhält den Anfangswert 0
#         self.max_inhalt = 1000
#         self.geöffnet = False
#     def öffnen(self):
#         self.geöffnet = True # 5 Das Attribut geöffnet erhält den Wert True. Die Flasche ist jetzt geöffnet
#     def schließen(self):
#         self.geöffnet = False
#     def füllen(self, volumen):
#         if self.geöffnet: # 6 Nur wenn die Flasche geöffnet ist, kann sie befüllt werden
#             if self.inhalt + volumen <= self.max_inhalt:
#                 self.inhalt += volumen # 7 Wenn das Volumen volumen noch in die Flasche passt, wird es dem inhalt hinzugefügt. Das Attribut inhalt bekommt dann einen neuen Wert.
#     def leeren(self):
#         if self.geöffnet:
#             self.inhalt = 0 # 8 Die Methode leeren() ist so definiert, dass die Flasche sich vollständig entleert
#
#
# b = Flasche() # Бутылка Бэ
# b.öffnen() # ОТКРЫВАЕМ БУТЫЛКУ БЭ
# b.füllen(500)  # НАПОЛНЯЕМ БУТЫЛКУ на 500 (уже 500 из 1000)
# b.füllen(1000) # НАПОЛНЯЕМ БУТЫЛКУ на 1000 (уже 1500 из 1000, перебор, а значит...)
# print(b.inhalt) # Выдаст 500, т.к. бутылка переполнена на 500
