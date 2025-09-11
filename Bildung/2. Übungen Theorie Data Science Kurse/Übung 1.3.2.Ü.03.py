X = [20,26,32,48,26,30,30,40] # Площадь квартиры в квадратных метрах
Y = [270,460,512,550,360,399,419,390] # Арендная плата (общая) с учетом стоимости за квадратный метр


import numpy as np

# === 7️⃣ Коэффициент корреляции Пирсона ===
corr_matrix = np.corrcoef(X, Y)  # Коэффициент корреляции
print("Корреляция Пирсона:", corr_matrix[0, 1])
# Корреляция идет к 1, значит, сильная связь, и значит, цена зависит от площади
# Interpretation: Der Korrelationskoeffizient ist positiv und größer als 0.5, weshalb ein starker Zusammenhang zwischen der Fläche und dem Mietpreis besteht.
