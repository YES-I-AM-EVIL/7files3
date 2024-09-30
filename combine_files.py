import os

def combine_files(input_files, output_file):
    """Функция для объединения файлов по заданным правилам."""
    file_info = []

    # Читаем содержимое каждого файла
    for filename in input_files:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            line_count = len(lines)
            file_info.append((filename, line_count, lines))

    # Сортируем файлы по количеству строк
    file_info.sort(key=lambda x: x[1])  # x[1] - количество строк

    # Записываем в итоговый файл
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename, line_count, lines in file_info:
            outfile.write(f"{filename}\n")  # Имя файла
            outfile.write(f"{line_count}\n")  # Количество строк
            outfile.writelines(lines)  # Содержимое файла
            outfile.write("\n")  # Добавляем пустую строку после содержимого файла

# Пример использования
if __name__ == '__main__':
    input_files = ['1.txt', '2.txt', '3.txt']  # Укажите имена ваших файлов
    output_file = 'combined.txt'  # Имя итогового файла
    combine_files(input_files, output_file)
    print(f"Файлы успешно объединены в '{output_file}'")
