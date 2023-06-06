import re

def formatted_numbers():
     
    decimal = 'decimal'
    hexa = 'hex'
    binary = 'binary'
    list_str = []
    list_str.append(f'|{decimal:^10}|{hexa:^10}|{binary:^10}|')

    for i in range(0,16):
        list_str.append(rf'|{int(i):<10}|{hex(i)[2]:^10}|{bin(i)[2:]:>10}|')
    return list_str
        
for el in formatted_numbers():
     print(el)