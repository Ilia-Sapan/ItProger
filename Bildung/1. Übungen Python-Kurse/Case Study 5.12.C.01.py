produkten = {
    "Laptop" : 99,
    "Smartphone" : 599,
    "Kopfhörer" : 149,
    "Smartwatch" : 249,
    "Tablet" : 399,
    "E-Book-Reader" : 129,
    "Fitness-Tracker" : 79,
    "Bluetoothlautsprecher" : 89,
    "Powerbank" : 39,
    "Webcam" : 59,
}
def durchschnittspreis(lists):
    sum_gesamt = sum(lists.values())  # Сумма всех цен
    lang_gesamt = len(lists)  # Количество продуктов
    mid = sum_gesamt / lang_gesamt  # Средняя цена
    return mid
def produkt_filter(buch, lists):
    result = []  # Список для хранения совпадений
    for key in lists:
        if key[0] == buch:  # Проверяем первый символ ключа
            result.append(key)
    return result  # Возвращаем список совпадений
def max_preis(lists):
    if not lists:
        return None
    # Базовый случай: если в списке один элемент
    if len(lists) == 1:
        return lists[0]
    maxi_preis = 0
    for value in lists.values():
        if value > maxi_preis:
            maxi_preis = value
    return maxi_preis
def preis_mit_steuer(lists, steuersatz = 0.19):
    spisok = []
    for values in lists.values():
        discount = values * steuersatz
        spisok.append(discount)
    return spisok
def preissteuer(lists, steuersatz = 0.35):
    neuen_preis = {key: value * (1 + steuersatz) for key, value in lists.items()}
    return neuen_preis

