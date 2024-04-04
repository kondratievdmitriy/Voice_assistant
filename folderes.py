import os
import shutil

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        return f"Папка {folder_name} успешно создана."
    else:
        return f"Папка {folder_name} уже существует."

def delete_folder(folder_name):
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)
        return f"Папка {folder_name} успешно удалена."
    else:
        return f"Папка {folder_name} не найдена."

def rename_folder(old_name, new_name):
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        return f"Папка {old_name} успешно переименована в {new_name}."
    else:
        return f"Папка {old_name} не найдена."

def list_files(folder_name):
    if os.path.exists(folder_name):
        files = os.listdir(folder_name)
        return f"Содержимое папки {folder_name}:\n{', '.join(files)}"
    else:
        return f"Папка {folder_name} не найдена."

def copy_files(src_folder, dest_folder):
    if os.path.exists(src_folder) and os.path.exists(dest_folder):
        files = os.listdir(src_folder)
        for file in files:
            shutil.copy(os.path.join(src_folder, file), dest_folder)
        return f"Файлы успешно скопированы из {src_folder} в {dest_folder}."
    else:
        return "Убедитесь, что обе папки существуют."

def delete_files(folder_name, filenames):
    if os.path.exists(folder_name):
        for filename in filenames:
            file_path = os.path.join(folder_name, filename)
            if os.path.exists(file_path):
                os.remove(file_path)
                return f"Файл {filename} успешно удален."
            else:
                return f"Файл {filename} не найден в папке {folder_name}."
    else:
        return f"Папка {folder_name} не найдена."

def search_files(folder_name, keyword):
    if os.path.exists(folder_name):
        files = os.listdir(folder_name)
        found_files = [file for file in files if keyword in file]
        if found_files:
            return f"Найдены файлы в папке {folder_name}, содержащие '{keyword}':\n{', '.join(found_files)}"
        else:
            return f"Файлы с ключевым словом '{keyword}' не найдены в папке {folder_name}."
    else:
        return f"Папка {folder_name} не найдена."