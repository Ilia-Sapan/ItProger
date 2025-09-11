eo1 = 0.8
eo2 = 0.5

w11 = 2.0
w12 = 1.0
w22 = 4.0
w21 = 3.0

def fehl_neuro(eo1, eo2, w11, w12, w21, w22):
    try:
        hidden_fehler = int(input("Номер скрытой ошибки (1 или 2): "))
        if hidden_fehler == 1:
            result_1 = eo1 * (w11 / (w11 + w21)) + eo2 * (w12 / (w12 + w22))
            return f'Скрытая ошибка равна {result_1:.2f}'
        elif hidden_fehler == 2:
            result_2 = eo1 * (w21 / (w11 + w21)) + eo2 * (w22 / (w12 + w22))
            return f'Скрытая ошибка равна {result_2}'
        else:
            return 'Введите правильное число!'
    except ValueError:
        return 'Ошибка!'

while True:
    print(fehl_neuro(eo1, eo2, w11, w12, w21, w22))
    cont = input("Хотите продолжить? (да/нет): ").strip().lower()
    if cont == "нет":
        break
