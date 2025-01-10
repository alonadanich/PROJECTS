"""
Завдання 1
Напишіть програму на Python, яка рекурсивно копіює файли у вихідній директорії, переміщає їх до нової директорії та сортує в піддиректорії, назви яких базуються на розширенні файлів.
Також візьміть до уваги наступні умови:
1. Парсинг аргументів. Скрипт має приймати два аргументи командного рядка: шлях до вихідної директорії та шлях до директорії призначення (за замовчуванням, якщо тека призначення не була передана, вона повинна бути з назвою dist).
2. Рекурсивне читання директорій:
Має бути написана функція, яка приймає шлях до директорії як аргумент.
Функція має перебирати всі елементи у директорії.
Якщо елемент є директорією, функція повинна викликати саму себе рекурсивно для цієї директорії.
Якщо елемент є файлом, він має бути доступним для копіювання.
3. Копіювання файлів:
Для кожного типу файлів має бути створений новий шлях у вихідній директорії, використовуючи розширення файлу для назви піддиректорії.
Файл з відповідним типом має бути скопійований у відповідну піддиректорію.
4. Обробка винятків. Код має правильно обробляти винятки, наприклад, помилки доступу до файлів або директорій.
"""
import os
import shutil
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Recursively move and sort files by extension.")
    parser.add_argument("source", help="Path to the source directory")
    parser.add_argument("destination", nargs='?', default=os.getenv('DEST_DIR', "dist"), help="Path to the destination directory (default: dist or value from DEST_DIR environment variable)")
    return parser.parse_args()

def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def move_and_sort_files(source, destination):
    ensure_directory(destination)
    for root, _, files in os.walk(source):
        for file in files:
            file_extension = os.path.splitext(file)[1][1:]  
            dest_dir = os.path.join(destination, file_extension)
            ensure_directory(dest_dir)
            shutil.move(os.path.join(root, file), os.path.join(dest_dir, file))

if __name__ == "__main__":
    args = parse_args()
    move_and_sort_files(args.source, args.destination)

