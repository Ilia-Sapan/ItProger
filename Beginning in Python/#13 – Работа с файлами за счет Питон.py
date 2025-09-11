# file = open("data/text.txt", "w") # "w" читает файлы, "a" добавляет
# file.write("Hello")
# file.write("!!!")
# # file.close()
# # data = input("Enter your text: ")
# # file = open("data/text.txt", "a") # "w" читает файлы, "a" добавляет
# # file.write(data + "\n")
# # file.close()
#
# file = open("data/text.txt", "r")
# print(file.read(1)) # параметр внутри функции read() выведет один символ. Чтобы читать весь текст, не пиши параметр
# file.close()

# Запись в файл
# with open("data/text.txt", "a") as file:
#     file.write("Hello!!!\n")  # Добавляем строку "Hello!!!"
#     data = input("Введите свой текст: ")
#     file.write(data + "\n")  # Добавляем текст пользователя с переводом строки
#
# # Чтение файла
# with open("data/text.txt", "r") as file:
#     print(file.read(1))    # Читаем и выводим первый символ

# with open("data/notes.txt", "a", encoding="utf-8") as file:
#     file.write("Привет\n")
#     file.write("Как дела?\n")

