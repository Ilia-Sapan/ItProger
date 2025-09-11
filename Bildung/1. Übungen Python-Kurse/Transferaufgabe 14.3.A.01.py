import datetime
from datetime import *

class Bankkonto:
    'ein Python-Programm, das ein einfaches Bankkonto-Management-System simuliert'
    inhaber = None
    konto_nr = None
    kontostand = float(0.00)
    transaktionen = []  # Список для хранения транзакций

    def __init__(self, inhaber, konto_nr, kontostand):
        # Конструктор класса Bankkonto, который инициализирует владельца, номер счета, баланс счёта
        self.inhaber = inhaber  # Присваиваем владельца
        self.konto_nr = konto_nr  # Номер счёта
        self.kontostand = kontostand  # Баланс счёта

    def einzahlen(self, summe, transaktionen):
        # Метод для внесения средств на счёт
        self.transaktionen = transaktionen  # Получаем список транзакций
        self.kontostand += summe  # Увеличиваем баланс
        aktuell_time = datetime.now()  # Получаем текущее время транзакции
        formatted_time = aktuell_time.strftime("%Y-%m-%d %H:%M:%S")  # Форматируем время
        self.transaktionen.append((formatted_time, self.kontostand))  # Добавляем транзакцию (время и новый баланс)

    def abheben(self, summe_minus):
        # Метод для снятия средств
        if summe_minus > self.kontostand:  # Проверка на достаточность средств
            print("Nicht genügend Guthaben")  # Если средств недостаточно
        else:
            self.kontostand -= summe_minus  # Снимаем средства
            aktuell_time = datetime.now()  # Получаем текущее время
            formatted_time = aktuell_time.strftime("%Y-%m-%d %H:%M:%S")  # Форматируем время
            self.transaktionen.append((formatted_time, self.kontostand))  # Добавляем транзакцию (время и новый баланс)

    def letzte_transaktionen(self):
        # Метод для получения последних 10 транзакций
        print(f"Последние десять транзакций: {self.transaktionen[-10:]}")  # Выводим последние 10 транзакций

    def get_info(self):
        # Метод для вывода информации о счёте
        print(f'Имя владельца: {self.inhaber} '
              f'\nНомер счёта: {self.konto_nr} '
              f'\nБаланс счёта: {self.kontostand} EUR '
              f'\nСписок транзакций: {self.transaktionen} '
              f'\nПоследние десять транзакций: {self.transaktionen[-10:]}')  # Выводим последние 10 транзакций


# Создаем объект класса Bankkonto
Ivan = Bankkonto('Ivan Sergeevich Golubev', 14567890, 100)



# def main():
#     konto = Bankkonto("Max Mustermann", "DE1234567890")
#     while True:
#         aktion = input("Wählen Sie eine Aktion: (E)inzahlen, (A)bheben, (T)ransaktionen anzeigen, (B)eenden: ").upper()
#         if aktion == "E":
#             betrag = float(input("Betrag zum Einzahlen: "))
#             konto.einzahlen(betrag)
#             print(f"{betrag}€ wurden eingezahlt.")
#         elif aktion == "A":
#             betrag = float(input("Betrag zum Abheben: "))
#             try:
#                 konto.abheben(betrag)
#                 print(f"{betrag}€ wurden abgehoben.")
#             except ValueError as e:
#                 print(e)
#         elif aktion == "T":
#             konto.letzte_transaktionen()
#         elif aktion == "B":
#             break
#         else:
#             print("Ungültige Aktion.")
#
#
# if __name__ == "__main__":
#     main()
