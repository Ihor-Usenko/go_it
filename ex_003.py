lst1 = [x for x in range(12)] # list comprihation
# lst1.append(10)
# print(lst1)
# lst1.append('11')
# print(lst1)          

lst1 = [1]

for i in lst1:
    lst1.append(1)
    print(len(lst1)) # !!! endless cycle !!!