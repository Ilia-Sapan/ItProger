
st_sp_pro_woche = [2,3,7,5,3]
import statistics
from statistics import stdev
stdev_sample = statistics.stdev(st_sp_pro_woche)  # Выборочное стандартное отклонение
stdev_population = statistics.pstdev(st_sp_pro_woche)  # Генеральное стандартное отклонение
print("Выборочное стандартное отклонение:", stdev_sample)
print("Генеральное стандартное отклонение:", stdev_population)