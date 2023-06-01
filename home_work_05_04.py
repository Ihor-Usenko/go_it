def is_check_name(fullname, first_name):
    result = fullname[0:len(first_name)]
    if result == first_name:
        return True
    else:
        return False
print(is_check_name('Alex Old', 'Alex'))



