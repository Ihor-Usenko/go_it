# def write_employees_to_file(employee_list, path):

#     file  = open(path, 'w')
#     for department in employee_list:
#         for emp in department:
#             file.write(emp + '\n')
#     file.close()





employee_list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
# employee_list = '\n'.join([i for sublist in employee_list for i in 
# sublist])
# fn = open('text.txt', 'w')
# fn.write(employee_list)
# fn.close()



# employee_list = '\n'.join([[emp for emp in department] for department in employee_list])
# employee_list = '\n'.join([[emp for emp in department] for department in employee_list])
fn = open('text.txt', 'w')
for list in employee_list:
    for i in list:
        fn.write(i + '\n')
fn.close()
