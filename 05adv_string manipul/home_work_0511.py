import re
from re import findall


text = "Guido van Rossum began working on PytHon in the late 1980s,\
      as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."
word = 'PythOn'
def find_all_words(text, word):
    coincidence = findall(word, text, flags = re.IGNORECASE)
    return coincidence

print(find_all_words(text, word))
