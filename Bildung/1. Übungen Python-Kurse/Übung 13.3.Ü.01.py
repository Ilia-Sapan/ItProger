# a



def filtere_gerade_zahlen(numbers_list) -> list:
    '''Die Funktion, die eine Liste von
    Zahlen als Argument nimmt und Liste
    mit dem gerade Zahle zurücknimmt'''
    assert type(numbers_list) is list
    numbers_list_new = []
    for num in numbers_list:
        if num % 2 == 0:
            numbers_list_new.append(num)
    return numbers_list_new

a = [1,2,3,4,5,6,7,8,9,10]
b = filtere_gerade_zahlen(a)
print(b)

# b

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

sortiere_liste(b)