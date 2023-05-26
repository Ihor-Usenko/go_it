# print('{name} {last_name}'.format(name='Igor', last_name='Usenko'))
# print('{0:d} {0:#b} {0:#x} {0:#o}'.format(10))
# print('{0:*^10}'.format('asd'))
# print('{0:*>10}'.format('asd'))
# print('{0:*<10}'.format('asd'))
# print('{0:^10}'.format('asd'))

# files = ['video.avi', 'audio.mp3', 'document.doc', 'folder', 'backup.tar.gz']
# for file in files:
#     try:
#         indx = file.rindex('.')
        
#         suffix = file[indx+1:]
#         print(f'File: {file} Index: {indx} Suffix: {suffix}')
    
#     except ValueError: 
#         print(f'File: {file} Suffix: not found')


'''list'''

lst2 = [1, 2, 3, 4]
lst1 = []
                   
for i in range(10):
    lst1.append(i)   

lst3 = []
for a in lst1:
    lst3.append(a)
    print(lst3)
