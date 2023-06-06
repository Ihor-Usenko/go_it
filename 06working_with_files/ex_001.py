# range_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# import re

# header = '|{:^15}|{:^15}|{:^15}|{:^15}|'.format('int', 'dex','oct', 'bin')
# separator = '-' * len(header)
# #print(separator, header, separator, sep='\n')
# body = ''
# for num in range_:
#     body += '|{0:^15d}|{0:^15x}|{0:^15o}|{0:^15b}|\n'.format(num)
# table = '\n'.join([separator, header, separator, body, separator])
# print(table)

# import re
# def total_salary(path):


#     list_string = []
#     sum_ = 0
#     fm = open(path,'r')
#     while True:
#         list_ = fm.readline()
#         list_string.append(list_)

#         if not list_:
#             break
#     fm.close()
#     list_string = ','.join(list_string)
#     list_string = re.findall(r'\d+', list_string)
#     for i in list_string:
#         sum_ += float(i)

#     return sum_
# print(total_salary('text.txt'))

import os
import shutil

def sort_files_by_extension(directory):
    # Создаем папку для каждого расширения, если она не существует
    for file_name in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file_name)):
            file_extension = os.path.splitext(file_name)[1]  # Получаем расширение файла
            folder_path = os.path.join(directory, file_extension[1:])  # Имя папки без точки в начале
            os.makedirs(folder_path, exist_ok=True)  # Создаем папку, если она не существует

    # Перемещаем файлы в соответствующие папки
    for file_name in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file_name)):
            file_extension = os.path.splitext(file_name)[1]  # Получаем расширение файла
            folder_path = os.path.join(directory, file_extension[1:])  # Имя папки без точки в начале
            source_path = os.path.join(directory, file_name)
            destination_path = os.path.join(folder_path, file_name)
            shutil.move(source_path, destination_path)  # Перемещаем файл в папку

# Пример использования
directory_path = '/путь/к/директории'
sort_files_by_extension(directory_path)

