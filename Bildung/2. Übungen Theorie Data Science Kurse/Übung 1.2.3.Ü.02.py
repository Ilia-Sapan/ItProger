import math

lists = ["k", "k", "k", "k", "k", "k", "k", "k", "k", "z"]

def enthropie (datei):
# Считаем количество каждого элемента
    count_k = datei.count("k")
    count_z = datei.count("z")

    # Общее количество элементов
    elements_zahl = len(datei)

    # Вычисляем вероятности для каждого элемента
    k_var = count_k / elements_zahl
    z_var = count_z / elements_zahl

    # Вычисляем энтропию
    entropy = 0
    if k_var > 0:
        entropy -= k_var * math.log2(k_var)
    if z_var > 0:
        entropy -= z_var * math.log2(z_var)

    # Выводим энтропию
    return entropy

print(f"Die Entropie des Datensatzes beträgt: {enthropie(lists):.4f} Bits")




def entropy(data):
    # Zähle, wie oft jedes Element vorkommt
    unique_elements = list(set(data))  # Einzigartige Elemente im Datensatz
    count = []
    probability_list = []

    # Zähle, wie oft jedes Element vorkommt und berechne die Wahrscheinlichkeit
    for element in unique_elements:
        element_count = data.count(element)
        count.append(element_count)
        probability_list.append(element_count / len(data))

    # Berechne die Entropie
    entropy_value = -sum(p * math.log2(p) for p in probability_list if p > 0)
    return entropy_value


# Beispiel: zehnmaliges Werfen einer Münze (Ergebnisse "Kopf" und "Zahl")
coin_toss = ["Kopf", "Zahl", "Kopf", "Kopf", "Zahl", "Zahl", "Kopf", "Zahl", "Kopf", "Zahl"]

# Entropie berechnen
print(f"Die Entropie des Datensatzes beträgt: {entropy(lists):.4f} Bits")

