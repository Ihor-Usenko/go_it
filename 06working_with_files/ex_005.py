from pathlib import Path

p = Path(r'c:\sorted')
arhcives = []
pictures = []
list_folders = []
list_files = []
suffix_in_folder = []
list_suffix = []
out_suffix = []

def get_files(p):

    for i in p.iterdir():
        if i.is_file():
            list_files.append(i)
        else:
            get_files(i)       
    return list_files
get_files(p)


for i in list_files:
    
    if i.suffix == '.zip' or i.suffix == '.gz' or i.suffix == '.tar':
        arhcives.append(i)
    if i.suffix == '.jpeg' or i.suffix == '.png' or i.suffix == '.jpg' or i.suffix == '.svg':
        pictures.append(i)
    




