

import numpy as np

umsatz = [3, 8, 19, 22, 31, 42, 48, 52, 54, 61]  # Выручка
verkaufsfläche = [150, 180, 420, 480, 660, 1000, 1300, 1500, 1600, 1710]  # Площадь продаж

# Вычисляем корреляционную матрицу
korrelationskoeffizient = np.corrcoef(umsatz, verkaufsfläche)

# Берём коэффициент корреляции (верхний правый или нижний левый элемент матрицы)
r = korrelationskoeffizient[0, 1]

# Проверяем уровень корреляции
if r >= 0.5:
    print(f"Es besteht eine ziemlich starke Korrelation zwischen Einnahmen und Verkaufsfläche, "
          f"Korrelationskoeffizient ist {r:.2f}")
else:
    print(f"Sehr schwache Korrelation ({r:.2f}), keine Korrelation.")


