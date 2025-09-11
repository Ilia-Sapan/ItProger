import math

def calculate_entropy(data):
    # Подсчитываем частоту каждого события
    weather_counts = {}
    for weather in data:
        if weather in weather_counts:
            weather_counts[weather] += 1
        else:
            weather_counts[weather] = 1

    # Общее количество дней
    total_days = len(data)

    # Расчет энтропии
    entropy = 0
    for count in weather_counts.values():
        probability = count / total_days
        entropy -= probability * math.log2(probability)

    return entropy

# Пример данных о погоде за 7 дней
weather_data = ['sonnig', 'regnerisch', 'bewölkt', 'sonnig', 'sonnig', 'regnerisch', 'regnerisch']

# Вызываем функцию
entropy = calculate_entropy(weather_data)
print(f"Энтропия данных: {entropy:.4f} бита")
