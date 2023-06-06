'''Dict'''

dct1 = {}
dct2 = dict()
dct3 = {1: 1, 2: 2, 3: 3}
dct4 = {x: x for x in range(10)}

persons = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "match": 175,
        "lang": 180,
        "end": 155,
    },
    {
        "name": "Ivanchuk Borislav",
        "specialty": 101,
        "match": 135,
        "lang": 150,
        "end": 165,
    },
    {   "name": "Karpenko Dmitro",
        "specialty": 201,
        "match": 155,
        "lang": 175,
        "end": 185,
    },
]

for person in persons:
    print(person.get('lang', 'Not found'))