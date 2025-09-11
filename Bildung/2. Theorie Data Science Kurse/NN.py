# import numpy as np
#
# # Входные сигналы
# vodka = 0.0
# rain = 1.0
# friend = 0.0
#
# # Функция активации
# def activation_funktion(x):
#     if x >= 0.5:
#         return 1
#     else:
#         return 0
#
# def predict(vodka, rain, friend):
#     inputs = np.array([vodka, rain, friend])
#
#     weights_input_to_hidden_1 = [0.25, 0.25, 0]
#     weights_input_to_hidden_2 = [0.5, -0.4, 0.9]
#     weights_input_to_hidden = np.array([weights_input_to_hidden_1, weights_input_to_hidden_2])
#
#     weights_hidden_to_output = np.array([-1, 1])
#
#     hidden_input = np.dot(weights_input_to_hidden, inputs)
#     print(f"Hidden input: {hidden_input}")
#
#     hidden_output = np.array([activation_funktion(x) for x in hidden_input])
#     print(f"Hidden output: {hidden_output}")
#
#     output = np.dot(weights_hidden_to_output, hidden_output)
#     print(f'Output: {output}')
#
#     return activation_funktion(output) == 1
#
# print(f'Result: {predict(vodka, rain, friend)}')
# Импортируем необходимые библиотеки:
import numpy as np  # numpy для математических операций с массивами
import sys        # sys для работы с системным выводом (например, для обновления строки прогресса)

# Определяем класс PartyNN, реализующий простую нейронную сеть:
class PartyNN(object):

    # Конструктор класса с параметром скорости обучения (learning_rate)
    def __init__(self, learning_rate=0.1):
        # Инициализируем веса между входным и скрытым слоями (матрица размером 2x3) с нормальным распределением,
        # стандартное отклонение рассчитывается как 2^-0.5
        self.weights_0_1 = np.random.normal(0.0, 2 ** -0.5, (2, 3))
        # Инициализируем веса между скрытым и выходным слоями (матрица размером 1x2) с нормальным распределением со стандартным отклонением 1
        self.weights_1_2 = np.random.normal(0.0, 1, (1, 2))
        # Создаём векторизированную функцию для применения сигмоидной функции ко всем элементам массива
        self.sigmoid_mapper = np.vectorize(self.sigmoid)
        # Преобразуем скорость обучения в массив numpy для удобства при операциях обновления весов
        self.learning_rate = np.array([learning_rate])

    # Определяем функцию активации - сигмоиду
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))  # Функция сигмоида преобразует любое число в интервал (0, 1)

    # Метод для получения предсказания сети на основе входных данных
    def predict(self, inputs):
        # Рассчитываем вход для скрытого слоя: скалярное произведение входных данных и весов первого слоя
        inputs_1 = np.dot(self.weights_0_1, inputs)
        # Применяем сигмоидную функцию ко входу скрытого слоя для получения его активаций
        outputs_1 = self.sigmoid_mapper(inputs_1)

        # Рассчитываем вход для выходного слоя: скалярное произведение активаций скрытого слоя и весов второго слоя
        inputs_2 = np.dot(self.weights_1_2, outputs_1)
        # Применяем сигмоидную функцию к выходу выходного слоя
        outputs_2 = self.sigmoid_mapper(inputs_2)
        # Возвращаем предсказание сети
        return outputs_2

    # Метод обучения сети по одному примеру с обратным распространением ошибки
    def train(self, inputs, expected_predict):
        # Прямой проход: вычисляем вход и выход скрытого слоя
        inputs_1 = np.dot(self.weights_0_1, inputs)
        outputs_1 = self.sigmoid_mapper(inputs_1)

        # Прямой проход: вычисляем вход и выход выходного слоя
        inputs_2 = np.dot(self.weights_1_2, outputs_1)
        outputs_2 = self.sigmoid_mapper(inputs_2)
        # Извлекаем скалярное предсказание (так как выходной слой состоит из одного нейрона)
        actual_predict = outputs_2[0]

        # Вычисляем ошибку на выходном слое: разница между фактическим и ожидаемым предсказанием
        error_layer_2 = np.array([actual_predict - expected_predict])
        # Вычисляем производную сигмоиды для выходного нейрона (градиент функции активации)
        gradient_layer_2 = actual_predict * (1 - actual_predict)
        # Определяем изменение весов (дельта) для выходного слоя по правилу градиентного спуска
        weights_delta_layer_2 = error_layer_2 * gradient_layer_2
        # Обновляем веса второго слоя, перемножая дельту на транспонированное значение активаций скрытого слоя,
        # умножаем на скорость обучения
        self.weights_1_2 -= (np.dot(weights_delta_layer_2, outputs_1.reshape(1, len(outputs_1)))) * self.learning_rate

        # Вычисляем ошибку для скрытого слоя, умножая дельту выходного слоя на веса второго слоя (обратное распространение)
        error_layer_1 = weights_delta_layer_2 * self.weights_1_2
        # Вычисляем градиент для скрытого слоя, аналогично сигмоиде
        gradient_layer_1 = outputs_1 * (1 - outputs_1)
        # Вычисляем дельту для весов первого слоя, перемножая ошибку и градиент для скрытого слоя
        weights_delta_layer_1 = error_layer_1 * gradient_layer_1
        # Обновляем веса первого слоя; здесь входные данные преобразуются в вектор-столбец для корректного умножения,
        # затем транспонируем результат и умножаем на скорость обучения
        self.weights_0_1 -= np.dot(inputs.reshape(len(inputs), 1), weights_delta_layer_1).T * self.learning_rate

# Функция для расчёта средней квадратичной ошибки (MSE) между предсказанными и ожидаемыми значениями
def MSE(y, Y):
    return np.mean((y - Y) ** 2)

# Набор данных для обучения (входы и соответствующие ожидаемые выходы)
train = [
    ([0, 0, 0], 0),
    ([0, 0, 1], 1),
    ([0, 1, 0], 0),
    ([0, 1, 1], 0),
    ([1, 0, 0], 1),
    ([1, 0, 1], 1),
    ([1, 1, 0], 0),
    ([1, 1, 1], 1),
]

# Количество эпох (итераций) обучения
epochs = 5000
# Определяем скорость обучения
learning_rate = 0.05

# Создаём экземпляр нейронной сети с заданной скоростью обучения
network = PartyNN(learning_rate=learning_rate)

# Основной цикл обучения нейронной сети по заданному числу эпох
for e in range(epochs):
    inputs_ = []              # Список для хранения входных данных текущей эпохи
    correct_predictions = []  # Список для хранения ожидаемых результатов для вычисления ошибки

    # Проходим по каждому примеру из тренировочного набора
    for input_stat, correct_predict in train:
        # Обучаем сеть на данном примере: передаем входной массив и ожидаемое значение
        network.train(np.array(input_stat), correct_predict)
        # Сохраняем входной пример для расчёта ошибки по всей эпохе
        inputs_.append(np.array(input_stat))
        # Сохраняем ожидаемое значение для расчёта средней ошибки
        correct_predictions.append(np.array(correct_predict))

    # Вычисляем среднюю квадратичную ошибку (MSE) по всем примерам эпохи; для этого транспонируем массив входов,
    # чтобы получить нужную форму для функции predict
    train_loss = MSE(network.predict(np.array(inputs_).T), np.array(correct_predictions))
    # Обновляем строку вывода, чтобы отобразить прогресс обучения (без перехода на новую строку)
    sys.stdout.write("\rProgress: {}, Training loss: {}".format(str(100 * e/float(epochs))[:4], str(train_loss)[:5]))

# После завершения обучения выводим результаты: для каждого входного примера показываем, правильно ли сеть классифицирует (с порогом 0.5)
for input_stat, correct_predict in train:
    print("For input: {} the prediction is: {}, expected: {}".format(
        str(input_stat),
        str(network.predict(np.array(input_stat)) > .5),  # сравнение предсказания с 0.5 для получения булева значения
        str(correct_predict == 1)))

# Выводим "сырые" значения предсказаний сети (без округления или порогового сравнения)
for input_stat, correct_predict in train:
    print("For input: {} the prediction is: {}, expected: {}".format(
        str(input_stat),
        str(network.predict(np.array(input_stat))),
        str(correct_predict == 1)))
