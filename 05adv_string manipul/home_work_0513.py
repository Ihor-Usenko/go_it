
import re

text = 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'

def find_all_emails(text):
    result = re.findall(r'[\w]*+@[a-zA-Z]*.[a-zA-Z]*.[a-zA-Z]+', text, re.ASCII)
    return result
print(find_all_emails(text))
