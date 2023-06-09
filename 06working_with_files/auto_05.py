with open('text.txt', 'r') as cats:
    
    dict_cat = []
    list_cats = cats.readlines()
    for i in list_cats:
        
        keys = ['id', 'name', 'age']
        i = tuple(i.strip().split(','))
        dictionary = dict(zip(keys, i))
        dict_cat.append(dictionary)
        
    return dict_cat


 
    














    # for i in cats:
    #     list_cats += i.split('\n')
    #     new_list_cats = list_cats[::2]
    # print(new_list_cats)
        #result = [{'id': d[0], 'name': d[1], 'number': d[2]} for d in data]

    
