articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]
def find_articles(key, letter_case=False):


    new_list = []

    for list_ in articles_dict:
        for i in list_.values():
            if type(i) == int:
                continue
            if letter_case == False:
                i = i.lower()
                key = key.lower()
            if i.find(key) != -1:
                new_list.append(list_)

    return new_list

print(find_articles('Ocean', True))