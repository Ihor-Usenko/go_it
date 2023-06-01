import re

text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."
spam_words = ['began', 'released', 'ssk']

text = re.sub('began', '*'*len('began'), text)

print(text)