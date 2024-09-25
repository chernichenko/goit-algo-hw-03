import os
import shutil
import sys

def copy_and_sort_files(src_dir, dest_dir):
    # Перебираємо всі елементи в директорії
    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)

        # Якщо елемент є директорією, викликаємо функцію рекурсивно
        if os.path.isdir(src_path):
            copy_and_sort_files(src_path, dest_dir)
        else:
            # Якщо елемент є файлом, копіюємо його
            try:
                ext = item.split('.')[-1]  # Отримуємо розширення файлу
                ext_dir = os.path.join(dest_dir, ext)  # Шлях до піддиректорії

                # Створюємо піддиректорію, якщо її ще немає
                os.makedirs(ext_dir, exist_ok=True)
                
                # Копіюємо файл у відповідну піддиректорію
                shutil.copy2(src_path, ext_dir)
            except Exception as e:
                print(f"Error copying file {src_path}: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_directory> [destination_directory]")
        return

    src_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else 'dist'

    # Перевірка, чи існує вихідна директорія
    if not os.path.isdir(src_dir):
        print(f"Source directory {src_dir} does not exist.")
        return

    # Запускаємо функцію копіювання та сортування файлів
    copy_and_sort_files(src_dir, dest_dir)

if __name__ == "__main__":
    main()