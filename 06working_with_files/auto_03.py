def read_employees_from_file(path):

    fn = open(path, 'r')
    list_employee = []
    for i in fn:
        list_employee += i.split('\n')
        new_list_employee = list_employee[::2]
    fn.close()
    return new_list_employee

    



