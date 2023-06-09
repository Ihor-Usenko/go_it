from pathlib import Path

p = Path(r'c:\sorted')
list_folders = []
list_file = []
suffix_in_folder = []
list_suffix = []
out_suffix = []

def get_files_and_folders(p):

    for i in p.iterdir():
        if i.is_file():
            list_file.append(i)
            suffix_in_folder.append(i.suffix)
        elif i.is_dir():
            list_folders.append(i)

        
        else:
            get_files_and_folders(i)
           
    return list_file, suffix_in_folder
get_files_and_folders(p)

print(suffix_in_folder)

        






