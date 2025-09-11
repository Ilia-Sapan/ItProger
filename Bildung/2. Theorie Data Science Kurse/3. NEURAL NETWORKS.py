
# 1. Нейрон как базовый элемент
# Главная идея: нейрон получает входные данные,
# вычисляет их взвешенную сумму и пропускает через функцию активации (например, сигмоиду)

import numpy as np

def sigmoid ( x ) :
    return 1 / ( 1 + np.exp ( - x ) )

# Пример простого нейрона

inputs = np.array ( [0.5, - 0.2, 0.1 ] )

weights = np.array( [0.4, 0.8, - 0.5 ] )

# Взвешенная сумма и активация

output_neuron = sigmoid( np.dot (inputs, weights))

print(f'Выход нейрона : {output_neuron}')

# 2. Передача сигналов (Forward Propagation)

# Идея: Данные последовательно проходят через слои сети: входной слой > скрытый слой > выходной слой
# На каждом этапе происходит умножение веса и функция активации

# Пример прямого прохода через один скрытый слой

input_vector = np.array([0.6, 0.1, 0.8])

# Случайно инициированные веса

w_input_hidden = np.random.uniform(-0.5, 0.5, (4,3)) # 4 нейрона скрытого слоя, 3 входа
w_hidden_output = np.random.uniform(-0.5, 0.5, (2,4)) # 2 нейрона выходного слоя, 4 скрытых

# Вычисление выходов скрытого слоя

hidden_input = np.dot(w_input_hidden, input_vector)
hidden_output = sigmoid(hidden_input)

# Вычисления выхода сети

final_input = np.dot(w_hidden_output, hidden_output)
final_output = sigmoid(final_input)

print(f'Выход сети (forward pass): {final_output}')


# 3. Трёхслойная нейронная сеть

# Идея: Архитектура сети с тремя слоями: входной, средний, выходной. Такой подход позволяет модели решать более сложные задачи

# Архитектура: 3 входа, 4 скрытых нейрона, 2 выходных нейрона

def forward_pass ( input_vector, w_ih, w_ho ):
    hidden = sigmoid(np.dot( w_ih, input_vector) )
    output = sigmoid( np.dot (w_ho, hidden) )
    return output

# Пример данных и весов

input_data = np.array([0.6, 0.1, 0.8])
w_input_hidden = np.random.uniform(-0.5, 0.5, (4,3))
w_hidden_output = np.random.uniform(-0.5, 0.5, (2,4))

output = forward_pass(input_data, w_input_hidden, w_hidden_output)

print("Выход трёхслойной сети:", output)

# 4. Обучение нейросети (Backpropagation)

# Идея: После прямого прохода вычисляется ошибка между предсказанным и желаемым результатом.
# Затем, с помощью обратного распределения ошибки корректируются веса по правилу градиентного спуска

# Обучающий пример для одного шага обучения

learning_rate = 0.1  # 🔧 Задаём скорость обучения — насколько сильно менять веса при ошибке

target = np.array([0, 1])  # 🎯 Целевой (желаемый) выход — например, [0, 1] означает "второй класс"

# === 🔁 ПРЯМОЙ ПРОХОД (Forward Pass) ===

inputs = input_data.reshape(-1, 1)  # 🔄 Преобразуем входной вектор в столбец (размер n×1)

hidden_input = np.dot(w_input_hidden, inputs)      # 🧠 Сигналы на скрытый слой: взвешенная сумма входов
hidden_output = sigmoid(hidden_input)              # ⚡ Применяем сигмоиду — активация скрытых нейронов

final_input = np.dot(w_hidden_output, hidden_output)  # 📡 Сигналы на выходной слой: из скрытого
final_output = sigmoid(final_input)                   # ⚡ Активация выходных нейронов

# === ❌ ВЫЧИСЛЕНИЕ ОШИБКИ ===

error = target.reshape(-1, 1) - final_output  # ❗ Ошибка: насколько выход сети отличается от нужного ответа

# === 📉 ОБРАТНОЕ РАСПРОСТРАНЕНИЕ: ГРАДИЕНТЫ ===

# 🔽 Градиент для выходного слоя: насколько нужно изменить каждый выходной нейрон
grad_output = error * final_output * (1 - final_output)  # формула градиента сигмоиды

# 🔧 Обновление весов между скрытым и выходом
w_hidden_output += learning_rate * np.dot(grad_output, hidden_output.T)  # ΔW = lr * δ * вход^T

# 🔽 Ошибка, идущая в скрытый слой (как выходные нейроны повлияли на скрытые)
hidden_error = np.dot(w_hidden_output.T, grad_output)

# 🔽 Градиент для скрытого слоя
grad_hidden = hidden_error * hidden_output * (1 - hidden_output)

# 🔧 Обновление весов между входом и скрытым слоем
w_input_hidden += learning_rate * np.dot(grad_hidden, inputs.T)

# ✅ Финальное сообщение
print("Обновленные веса (пример обучения) выполнены")



# 5. Программирование нейронной сети «с нуля»
# Идея: Реализовать всю архитектуру и алгоритм обучения без готовых фреймворков –
# отличный способ понять работу нейросетей на базовом уровне.

# Простая нейросеть с одним скрытым слоем:

class SimpleNeuralNetwork:

    def __init__(self, input_size, hidden_size, output_size, learning_rate):
        # Сохраняем скорость обучения
        self.learning_rate = learning_rate

        # 🎲 Случайная инициализация весов: вход -> скрытый слой
        # Размер матрицы: (нейронов в скрытом слое) × (входов)
        self.w_input_hidden = np.random.uniform(-0.5, 0.5, (hidden_size, input_size))

        # 🎲 Случайная инициализация весов: скрытый -> выход
        # Размер: (выходов) × (нейронов в скрытом слое)
        self.w_hidden_output = np.random.uniform(-0.5, 0.5, (output_size, hidden_size))

    def forward(self, input_vector):
        # 🔄 Преобразуем вход в столбец
        self.input = input_vector.reshape(-1, 1)

        # 🧠 Скрытый слой: взвешенная сумма + сигмоида
        self.hidden = sigmoid(np.dot(self.w_input_hidden, self.input))

        # 🧠 Выходной слой: снова взвешенная сумма + сигмоида
        self.output = sigmoid(np.dot(self.w_hidden_output, self.hidden))

        # 🎯 Возвращаем предсказание
        return self.output

    def train(self, input_vector, target_vector):
        # 🔁 Запускаем прямой проход (получаем текущий вывод)
        output = self.forward(input_vector)

        # 🎯 Целевой ответ в виде столбца
        target = target_vector.reshape(-1, 1)

        # ❌ Ошибка между целевым и фактическим выходом
        error = target - output

        # 🔁 Градиент ошибки для выходного слоя
        grad_output = error * output * (1 - output)

        # 🔧 Обновляем веса скрытый -> выходной слой
        self.w_hidden_output += self.learning_rate * np.dot(grad_output, self.hidden.T)

        # 🧠 Ошибка, переданная обратно в скрытый слой
        hidden_error = np.dot(self.w_hidden_output.T, grad_output)

        # 🔁 Градиент ошибки для скрытого слоя
        grad_hidden = hidden_error * self.hidden * (1 - self.hidden)

        # 🔧 Обновляем веса вход -> скрытый слой
        self.w_input_hidden += self.learning_rate * np.dot(grad_hidden, self.input.T)

# === 🚀 Пример использования ===

# Инициализируем нейросеть: 3 входа, 4 скрытых нейрона, 2 выхода
nn = SimpleNeuralNetwork(input_size=3, hidden_size=4, output_size=2, learning_rate=0.1)

# Прогоняем вход до обучения
print("Начальный вывод сети:", nn.forward(np.array([0.6, 0.1, 0.8])).flatten())

# Обучаем сеть на одном примере с целевым выходом [1, 0]
nn.train(np.array([0.6, 0.1, 0.8]), np.array([1, 0]))

# Смотрим, как изменился выход после обучения
print("Вывод сети после обучения:", nn.forward(np.array([0.6, 0.1, 0.8])).flatten())


