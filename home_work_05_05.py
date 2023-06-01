# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#         .removeprefix("+")
#         .replace("(", "")
#         .replace(")", "")
#         .replace("-", "")
#         .replace(" ", "")
#     )
#     return new_phone

# phone_number = ['+81(067)230 04 01', '+65(063)230 04 01', '+88(063)230 04 01','+38(063)230 04 01',\
#                  '+48(063)230 04 01']

# def get_phone_numbers_for_countries(list_phones):
#     japan = []
#     singapore = []
#     taiwan = []
#     ukraine = []
#     list_for_sort = []
#     for i in phone_number:
#         list_for_sort.append(sanitize_phone_number(i))


#     for i in list_for_sort:
#         if i[0:2] == '81':
#             japan.append(i)
#         elif i[0:2] == '65':
#             singapore.append(i)
#         elif i[0:2] == '88':
#             taiwan.append(i)
#         else:
#             ukraine.append(i)

#     final_dict = {'JP': japan, 'SG': singapore, 'TW': taiwan, 'UA': ukraine}
#     return final_dict

# print(get_phone_numbers_for_countries(phone_number))
import re
text = 'Молох бог ужасен лох.'
i = 'лох'



result = re.findall(r'\Bлох'.format(i), text)
print(result)
  
        





