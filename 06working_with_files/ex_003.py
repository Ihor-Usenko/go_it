import os
folders = []
files = []
def get_files_and_folders(directory):
    files_and_folders = []
    for root, directories, files in os.walk(directory):
        for file in files:
            files_and_folders.append(os.path.join(root, file))
        for folder in directories:
            files_and_folders.append(os.path.join(root, folder))
    for i in files_and_folders:
        
        print(i)

# Пример использования
get_files_and_folders('c:\sorted')
