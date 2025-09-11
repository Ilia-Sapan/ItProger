import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# === 1. Функция активации (сигмоида) ===
# Преобразует любое значение в диапазон (0, 1)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# === 2. Функция обучения одного примера ===
def train(input_vector, w_ih, w_ho, target_vector, lr):
    # Преобразуем входной вектор в столбец
    inputs = np.array(input_vector, ndmin=2).T
    targets = np.array(target_vector, ndmin=2).T

    # Скрытый слой: сигналы и активация
    hidden_inputs = np.dot(w_ih, inputs)
    hidden_outputs = sigmoid(hidden_inputs)

    # Выходной слой: сигналы и активация
    final_inputs = np.dot(w_ho, hidden_outputs)
    final_outputs = sigmoid(final_inputs)

    # Ошибки на выходе
    output_errors = targets - final_outputs

    # Ошибки скрытого слоя (обратное распространение)
    hidden_errors = np.dot(w_ho.T, output_errors)

    # Обновление весов скрытый -> выход
    w_ho += lr * np.dot((output_errors * final_outputs * (1 - final_outputs)),
                        hidden_outputs.T)

    # Обновление весов вход -> скрытый
    w_ih += lr * np.dot((hidden_errors * hidden_outputs * (1 - hidden_outputs)),
                        inputs.T)

# === 3. Функция прямого прохода (для тестирования) ===
def feedforward(input_vector, w_ih, w_ho):
    inputs = np.array(input_vector, ndmin=2).T
    hidden_outputs = sigmoid(np.dot(w_ih, inputs))
    final_outputs = sigmoid(np.dot(w_ho, hidden_outputs))
    return final_outputs

# === 4. Загрузка датасета MNIST из CSV ===
df = pd.read_csv(r"C:\Users\isapa\Desktop\DS Kurse\Kursmaterial für Übungen\K4.0026_2.0_3.5.Ü.01_mnist_data.csv", header=None)
data_list = df.values.tolist()

# === 5. Разделение меток и пиксельных данных ===
label_list = [row[0] for row in data_list]         # метки: 0–9
pixel_data = [row[1:] for row in data_list]        # 784 пикселя

# === 6. Нормализация данных и разделение на train/test ===
train_data = (np.asarray(pixel_data[:8000]) / 255 * 0.99) + 0.01
train_labels = label_list[:8000]

test_data = (np.asarray(pixel_data[8000:]) / 255 * 0.99) + 0.01
test_labels = label_list[8000:]

# === 7. Параметры нейросети ===
input_nodes = 784        # 28x28 пикселей
hidden_nodes = 100       # скрытых нейронов
output_nodes = 10        # выходов (0–9)
learning_rate = 0.1      # скорость обучения

# === 8. Инициализация весов случайными значениями ===
w_input_hidden = np.random.uniform(-0.5, 0.5, (hidden_nodes, input_nodes))
w_hidden_output = np.random.uniform(-0.5, 0.5, (output_nodes, hidden_nodes))

# === 9. Обучающий цикл ===
for i in range(len(train_data)):
    # Создаём one-hot вектор цели (например, [0.01, ..., 0.99, ..., 0.01])
    targets = np.zeros(output_nodes) + 0.01
    targets[int(train_labels[i])] = 0.99

    # Обучаем сеть на этом примере
    train(train_data[i], w_input_hidden, w_hidden_output, targets, learning_rate)

    # Печатаем прогресс обучения
    if i % 1000 == 0:
        print(f"Обучение {i}/{len(train_data)}...")

print("\nОбучение завершено.")

# === 10. Тестируем на первом примере из тестовой выборки ===
output = feedforward(test_data[0], w_input_hidden, w_hidden_output)
predicted = np.argmax(output)        # выбираем индекс с наибольшим значением
real = test_labels[0]                # реальная метка

print("Сеть предсказала:", predicted)
print("Реальное значение:", real)

# === 11. Визуализация изображения ===
image = np.array(test_data[0]).reshape(28, 28)
plt.imshow(image, cmap='gray')
plt.title(f"Сеть думает: {predicted} | Реально: {real}")
plt.axis("off")
plt.show()
