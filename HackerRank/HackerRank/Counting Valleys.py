


def countingValleys(steps, path):
    altitude = 0
    valleys = 0
    for step in path:
        if step == 'U':
            altitude += 1  # Подъем на 1
        elif step == 'D':
            altitude -= 1  # Спуск на 1


        if altitude == 0 and step == 'U':
            valleys += 1

    return valleys

