import matplotlib.pyplot as plt
import statistics as st

# Исходные данные
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

# # Вычисляем средние значения
# mean_x = st.mean(x)
# mean_y = st.mean(y)
#
# # Вычисляем коэффициент наклона (result) и свободный член (a)
# summary_high = 0
# summary_low = 0
# for xi, yi in zip(x, y):
#     summary_high += (xi - mean_x) * (yi - mean_y)
#     summary_low += (xi - mean_x) ** 2
#
# result = summary_high / summary_low
# a = mean_y - result * mean_x
#
# # Вычисляем предсказанные значения y по модели линейной регрессии
# y_pred = [a + result * xi for xi in x]

# # Строим график
# plt.scatter(x, y, label='Исходные данные')
# plt.plot(x, y_pred, color='red', label='Линия регрессии')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Линейная регрессия')
# plt.legend()
# plt.show()

def determine(x, y):
    # Вычисляем средние значения
    mean_x = st.mean(x)
    mean_y = st.mean(y)

    # Вычисляем коэффициент наклона (result) и свободный член (a)
    summary_high = 0
    summary_low = 0
    for xi, yi in zip(x, y):
        summary_high += (xi - mean_x) * (yi - mean_y)
        summary_low += (xi - mean_x) ** 2

    result = summary_high / summary_low
    a = mean_y - result * mean_x

    # Вычисляем предсказанные значения y по модели линейной регрессии
    y_pred = [a + result * xi for xi in x]

    # Вычисляем суммы квадратов остатков и общей суммы квадратов
    ssres = 0
    sstot = 0
    for actual, predicted in zip(y, y_pred):
        ssres += (actual - predicted) ** 2
        sstot += (actual - mean_y) ** 2

    # Вычисляем коэффициент детерминации R^2
    R = 1 - (ssres / sstot)
    return R

print(determine(x, y))
