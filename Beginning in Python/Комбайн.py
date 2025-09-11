import os

# Список папок для поиска
directories = ["C:\\Users\\isapa\\Documents\\Obsidian Vault\\Für die Überlegung",
               "C:\\Users\\isapa\\Documents\\Obsidian Vault\\Hauptverzeichnis"]
output_file = 'combined.md'

# Открываем итоговый файл для записи
with open(output_file, 'w', encoding='utf-8') as outfile:
    for directory in directories:
        # Проходим по всем вложенным папкам
        for root, _, files in os.walk(directory):
            # Фильтруем только .md файлы
            md_files = sorted([f for f in files if f.endswith('.md')])
            for file in md_files:
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as infile:
                    # Добавляем разделитель между файлами (опционально)
                    outfile.write(f"\n\n# {file}\n\n")
                    outfile.write(infile.read())

print(f"Объединение завершено. Файл сохранён как {output_file}")
