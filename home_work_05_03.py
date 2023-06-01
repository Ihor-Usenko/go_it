def sanitize_phone_number(phone):
    new_phone = ''

    for i in phone:
        if i.isdigit():
            new_phone += i
        else:
            continue
    return new_phone

print(sanitize_phone_number("     0503451234"))