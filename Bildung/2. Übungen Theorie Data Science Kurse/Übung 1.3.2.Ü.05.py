# Programmiere eine Python-Funktion, die die Kovarianz zwischen zwei Listen von Datenwerten berechnen kann.
import numpy as np
# def cov (x,y):
#     def mean_values(liste):
#         mean_value = sum(liste) / len(liste)
#         return mean_value
#     x_ = mean_values(x)
#     y_ = mean_values(y)
#     x_1 = sum((el - mean_values for el in x))
#     y_1 = sum((el - mean_values for el in y))
#     gesamt = (x_1 * y_1) / len(x)
#     return gesamt


def cov(x, y):
    def mean_values(liste):
        return sum(liste) / len(liste)  # Среднее значение списка

    x_mean = mean_values(x)  # Среднее по X
    y_mean = mean_values(y)  # Среднее по Y

    # Формула: Cov(X, Y) = Σ (Xi - X̄) * (Yi - Ȳ) / n
    cov_value = sum((x_i - x_mean) * (y_i - y_mean) for x_i, y_i in zip(x, y)) / len(x)

    return cov_value


# Тестируем
x = [3, 8, 19, 22, 31]
y = [150, 180, 420, 480, 660]

print("Ковариация:", cov(x, y))  # Теперь считает правильно!

X = [3, 8, 19, 22, 31]  # 5 элементов
Y = [150, 180, 420, 480, 660]  # 5 элементов

real = np.cov(X, Y, ddof=0)  # Генеральная ковариация
print("Result official: ", real)

# ERRORS

# ❌ mean_values — это функция, а не число!
# Ты должен вычитать x_, а не mean_values.
# ❌ Ошибка в sum(), нужно () после mean_values.
# ❌ Формула ковариации неправильная:
# x_1 * y_1 — это не сумма произведений отклонений, а просто произведение сумм!

