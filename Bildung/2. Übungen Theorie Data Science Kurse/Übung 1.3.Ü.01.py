

a = [2,3,4,1,4,2,4,5,5,5,5,2,1,1,2,2,2,2,5,4,5,21,2]

b = ["groß", "klein", "mittel", "groß", "groß", "klein", "mittel", "mittel", "mittel", "groß", "groß", "klein", "klein"]

c =  ["ja", "nein", "nein", "ja", "nein", "ja", "ja", "ja", "nein"]

import  statistics
from statistics import mode

print(f"Innerhalb dieser Daten ist der Modus von A ist {statistics.mode(a)},"
      f" der Modus von B ist gleich '{statistics.mode(b)}' "
      f"und der Modus von C ist gleich '{statistics.mode(c)}'")

# 2

import statistics

a = [1, 1, 1, 1, 1,
 2, 2, 2, 2, 2, 2,
 3, 3,
 4,
 5, 5, 5, 5, 5, 5]


print(statistics.median(a))