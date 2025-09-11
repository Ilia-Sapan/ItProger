import math

def cov(x, y):
    def mean_values(liste):
        return sum(liste) / len(liste)  # Среднее значение списка

    x_mean = mean_values(x)  # Среднее по X
    y_mean = mean_values(y)  # Среднее по Y

    # Формула: Cov(X, Y) = Σ (Xi - X̄) * (Yi - Ȳ) / n
    cov_value = sum((x_i - x_mean) * (y_i - y_mean) for x_i, y_i in zip(x, y)) / len(x)

    return cov_value



def corr_koef(x,y):
    def cov(x, y):
        def mean_values(liste):
            return sum(liste) / len(liste)  # Среднее значение списка

        x_mean = mean_values(x)  # Среднее по X
        y_mean = mean_values(y)  # Среднее по Y

        # Формула: Cov(X, Y) = Σ (Xi - X̄) * (Yi - Ȳ) / n
        cov_value = sum((x_i - x_mean) * (y_i - y_mean) for x_i, y_i in zip(x, y)) / len(x)

        return cov_value
    def standardabweichung(liste):
        mean_value = sum(liste) / len(liste)  # Среднее арифметическое
        variance = sum((el - mean_value) ** 2 for el in liste) / len(liste)  # Дисперсия
        return math.sqrt(variance)  # Корень из дисперсии = стандартное отклонение

    a = cov(x, y)
    y_ = standardabweichung(y)
    x_ = standardabweichung(x)

    result = a / (x_ * y_)
    return result


# Тестовые данные
x = [3, 8, 19, 22, 31]
y = [150, 180, 420, 480, 660]

print("Коэффициент корреляции:", corr_koef(x, y))