grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):

    list_ = []
    n = 1
    for i, v in zip(students, students.values()):
        list_.append('{:>4}|{:<10}|{:^5}|{:^5}'.format(n, i, v, grades[v]))
        n += 1
    return list_
    
