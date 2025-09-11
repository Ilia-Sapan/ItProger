try:
    with open("data/notes.txt", "r", encoding="utf-8") as file:
        print(file.read())
finally:
    print("Thanks!")