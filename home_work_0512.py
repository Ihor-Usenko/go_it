import re

text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."
spam_words = ['began', 'released', 'ssk']

def replace_spam_words(text, spam_words):
    
    for i in spam_words:
        if i in text:
            text = re.sub(i, '*'*len(i), text, flags = re.IGNORECASE)
    return text
