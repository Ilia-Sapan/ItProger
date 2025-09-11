import random


def sortiere_liste(list_must_be_sorted) -> list:
    if len(list_must_be_sorted) < 1:
        return list_must_be_sorted
    else:
        pivot = list_must_be_sorted[0]
        l_s_1 = [x for x in list_must_be_sorted[1:] if x < pivot]
        l_s_2 = [x for x in list_must_be_sorted[1:] if x > pivot]

        print(f"Ich sortiere: {list_must_be_sorted}")
        print('Aufspaltung:', l_s_1, pivot, l_s_2)
        return sortiere_liste(l_s_1) + [pivot] + sortiere_liste(l_s_2)

sss = [22,55,33,55,121,423,12433124]

print(sortiere_liste(sss))