'''Напишіть функцію real_len, яка підраховує та повертає довжину рядка без наступних керівних символів: [\n, \f, \r, \t, \v]

Для перевірки правильності роботи функції real_len їй будуть передані наступні рядки:

'Alex\nKdfe23\t\f\v.\r'
'Al\nKdfe23\t\v.\r'            '''



text = 'Al\nKdfe23\t\v.\r'

text1 = text.split()
text2 = ''.join(text1)

print(len(text2))



