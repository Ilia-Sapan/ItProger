import os
from contextlib import chdir
from os import getcwd, listdir

chdir(path=) Меняет текущую рабочую директорию на указанную в path.
os.chdir('/home/user/documents')  # Переход в указанный каталог

getcwd() Возвращает текущую рабочую директорию.
print(os.getcwd())  # Например, '/home/user'

listdir(path=) Возвращает список файлов и папок в указанной директории. Если путь не указан, берётся текущая директория.
print(os.listdir('/home/user'))  # ['file1.txt', 'folder', 'script.py']

path.exsist(path) Проверяет, существует ли путь (файл или директория).
print(os.path.exists('/home/user/file.txt'))  # True или False

path.gettime(path) Возвращает время создания файла или директории в формате timestamp (секунды с 1970 года).
print(os.path.getctime('/home/user/file.txt'))

path.getsize(path) Возвращает размер файла в байтах.
print(os.path.getsize('/home/user/file.txt'))  # Например, 1024 (1 КБ)

path.isdir(path) Проверяет, является ли путь директорией.
print(os.path.isdir('/home/user/documents'))  # True или False

path.isfile(path) Проверяет, является ли путь файлом.
print(os.path.isfile('/home/user/file.txt'))  # True или False

path.splitext(p) Разделяет путь на имя файла и его расширение.
print(os.path.splitext('/home/user/file.txt'))  # ('/home/user/file', '.txt')

walk(top) Рекурсивно обходит каталог top, возвращая пути к файлам и подпапкам.
for root, dirs, files in os.walk('/home/user'):
    print(f'В каталоге {root} найдены папки {dirs} и файлы {files}')

import os  # Импортируем модуль os для работы с файловой системой

print("Unterverzeichnisse: ")  # Выводит заголовок "Unterverzeichnisse: " (по-немецки "Подкаталоги:")

inhalt = os.listdir()  # Получаем список всех файлов и папок в текущей директории

for item in inhalt:  # Перебираем все элементы (файлы и папки)
    if os.path.isdir(item):  # Проверяем, является ли элемент директорией
        print(item)  # Если да, выводим его название

# platzbedarf.py
# import os  # Импортируем модуль os для работы с файловой системой
#
# # Создаём строку-шаблон для отчёта, куда позже подставим реальные значения
# BERICHT = '''
# Ich habe {} Verzeichnisse durchsucht.
# Der gesamte Speicherbedarf beträgt {} Bytes.
# '''
#
# # Функция для вычисления занимаемого места и количества директорий
# def berechne_platzbedarf(wurzel):
#     anzahl = 0 # Количество посещённых директорий
#     platz = 0 # Общий размер файлов в байтах
#     for v, _, d in os.walk(wurzel):  # Перебираем все подпапки и файлы
#         anzahl += 1  # Увеличиваем счётчик директорий
#         for datei in d:
#             platz += os.path.getsize(os.path.join(v, datei))  # Используем полный путь
#     return anzahl, platz  # Теперь return срабатывает после обработки всех директорий
#
#     # for v, uv, d in durchlauf:  # Перебираем директории, их подпапки и файлы
#     #     anzahl += 1  # Увеличиваем счётчик директорий
#     #     os.chdir(v)  # Меняем текущую директорию на `v` (❌ Это лишнее, см. ниже)
#     #
#     #     for datei in d:  # Перебираем файлы в текущей директории
#     #         platz += os.path.getsize(datei)  # Получаем размер файла и суммируем
#     #
#     #     return anzahl, platz  # ❌ Ошибка! Возвращает значения после первой итерации
#
#
# # Главная часть программы
# wurzel = input("Wurzelverzeichnis: ")  # Запрашиваем у пользователя путь к папке
#
# if os.path.exists(wurzel):  # Проверяем, существует ли введённый путь
#     anz_verz, speicher = berechne_platzbedarf(wurzel)  # Вызываем функцию
#     print(BERICHT.format(anz_verz, speicher))  # Выводим отчёт с подставленными значениями
# else:
#     print('Ungültiger Pfad')  # Если путь не существует, выводим сообщение об ошибке
#
# input()  # Ждём нажатия клавиши перед закрытием (актуально для Windows)

# Все каталоги (относительные пути) в дереве каталогов,
# корнем которого является текущий рабочий каталог.
# текущий рабочий каталог
# v1 = [i for i in os.listdir() if os.path.isdir(i)]
# # Все файлы в текущем рабочем каталоге, к которым обращались в течение последнего часа
# v2 = [i for i in os.listdir() if time.time() - os.path.getatime(i)>3600]

# 10.3 Dateien und Verzeichnisse anlegen und umbenennen

mkdir(path) # Создаёт новую папку (директорию) по указанному пути path.
os.mkdir("neue_ordner")  # Создаст папку "neue_ordner"

remove(path) # Удаляет файл по указанному пути path. Если путь указывает на папку, возникнет ошибка.
os.remove("datei.txt")  # Удалит файл "datei.txt"

removedirs(path) # Удаляет указанную папку и все пустые родительские директории. Если папка не пуста, возникнет ошибка.
os.removedirs("ordner1/ordner2")  # Удалит "ordner2" и "ordner1", если они пустые

rename(old, new) # Переименовывает или перемещает файл/папку из old в new.
os.rename("alte_datei.txt", "neue_datei.txt")  # Переименует файл

rmdir(path) # Удаляет только пустую папку. если в папке есть файлы, возникает ошибка
os.rmdir("leere_ordner")  # Удалит пустую папку "leere_ordner"

# 10.4 Das Modul sys – die Schnittstelle zum Laufzeitsystem

sys.argv — список аргументов командной строки, переданных при запуске скрипта.
import sys
print(sys.argv)  # Выводит список аргументов, например: ['script.py', 'arg1', 'arg2']

sys.executable — путь к исполняемому файлу Python.
print(sys.executable)  # Например: '/usr/bin/python3' или 'C:\\Python39\\python.exe'

sys.exit() — завершает выполнение программы.
print("Программа завершается")
sys.exit()
print("Этот код уже не выполнится")

sys.getrefcount(objekt) — возвращает количество ссылок на объект в памяти (используется для отладки).
a = []
print(sys.getrefcount(a))  # Например, 2 (из-за передачи в функцию print)

sys.platform — возвращает название операционной системы.
print(sys.platform)  # Например, 'win32' (Windows), 'linux' (Linux), 'darwin' (MacOS)

sys.stdin — стандартный ввод (например, input()).
sys.stdout — стандартный вывод (обычно print()).
sys.stderr — стандартный поток ошибок.

sys.version — информация о версии Python.
print(sys.version)  # Например: '3.10.4 (default, Mar 16 2022, 14:00:00) [GCC 9.3.0]'










