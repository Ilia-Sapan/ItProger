def train(input_list, w_ih, w_ho, target_list, learning_rate):
    # ⬇️ Преобразуем входной и целевой векторы в столбцы (2D)
    input_vector = numpy.array(input_list, ndmin=2).T
    targets = numpy.array(target_list, ndmin=2).T

    # 🔹 Прямой проход (Forward pass)

    # Вычисляем сигналы на скрытом слое
    input_hidden = numpy.dot(w_ih, input_vector)

    # Применяем сигмоиду для получения выходов скрытого слоя
    output_hidden = scipy.special.expit(input_hidden)

    # Вычисляем сигналы на выходном слое (ещё без активации)
    input_final = numpy.dot(w_ho, output_hidden)

    # Применяем сигмоиду к выходному слою — получаем окончательные выходы
    output_final = scipy.special.expit(input_final)

    # 🔻 Ошибки

    # Ошибка выходного слоя: как далеко от правильного ответа
    output_errors = targets - output_final

    # Ошибка скрытого слоя: как сильно повлияли скрытые нейроны на ошибку выхода
    hidden_errors = numpy.dot(w_ho.T, output_errors)

    # 🔄 Обновление весов

    # Обновляем веса между скрытым и выходным слоями
    # dW = lr * ошибка * выход * (1 - выход) * вход^T
    w_ho += learning_rate * numpy.dot(
        (output_errors * output_final * (1 - output_final)),
        numpy.transpose(output_hidden)
    )

    # Обновляем веса между входом и скрытым слоем
    w_ih += learning_rate * numpy.dot(
        (hidden_errors * output_hidden * (1 - output_hidden)),
        numpy.transpose(input_vector)
    )
