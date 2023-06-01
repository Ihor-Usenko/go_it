from re import search
text = "Guido van Rossum began working on Python in the late 1980s,\
        as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."
word = 'Python'

def find_word(text, word):
    find_word = search(word, text)
    if find_word == None:
        result_ = False
        first_index_ = None
        last_index_ = None
        search_string_ = word
        string_ = text
        list_result = {'result': result_, 'first_index': first_index_, 'last_index': 
        last_index_, 'search_string': search_string_, 'string': string_}
    else:
        result_ = True
    
        first_index_ = find_word.span()[0]
        last_index_ = find_word.span()[1]
        search_string_ = word
        string_ = text
        list_result = {'result': result_, 'first_index': first_index_, 'last_index': 
        last_index_, 'search_string': search_string_, 'string': string_}
    return list_result

print(find_word(text, word))