arr = [4, 2, 2, 8, 3, 3, 1]


def countingSort(arr):

    freq_array = [0] * 100


    for num in arr:
        if 0 <= num < 100:
            freq_array[num] += 1

    return freq_array

print(countingSort(arr))