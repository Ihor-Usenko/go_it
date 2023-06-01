import re


# def is_spam_words(text, spam_words, space_around=False):
    
#     text = text.casefold()
#     for i in spam_words:
#         if space_around == False:
#             result = re.findall(fr'{i}', text)
#             if result:
#                 return True
#         elif space_around == True:
#             result = re.findall(fr'\s{i}', text)
#             if result:
#                 return True
#     return False

CYRILLIC = ("а", "ч", "ш")
LATIN = ("a", "ch", "sh")

TRANSLIT_DICT = {}

for c, l in zip(CYRILLIC, LATIN):
    TRANSLIT_DICT[ord(c)] = l
    TRANSLIT_DICT[ord(c.upper())] = l.upper()

print(TRANSLIT_DICT) # chasha
print("ИГОРЬ".translate(TRANSLIT_DICT))  # CHASHA

