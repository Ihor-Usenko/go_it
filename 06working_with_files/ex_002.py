



import os
import shutil
file_extension = []
source_path = []
for file_name in os.listdir('c:\\sorted'):
        if os.path.isfile(os.path.join('c:\\sorted', file_name)):
            file_extension.append(os.path.splitext(file_name)[1])            # Получаем расширение файла
            source_path.append(os.path.join('c:\\sorted', file_name))
            #print(file_extension)
print(source_path)
        