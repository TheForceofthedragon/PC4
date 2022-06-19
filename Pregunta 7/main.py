# Importamos librerias
import email.utils
import re

def is_valid_email(text):
    pattern = r'^[a-z][a-z0-9\-_\.]+[@][a-z]+[.][a-z]{1,3}$'
    
    return re.search(pattern, text)

if __name__ == '__main__':
    contacts = [input() for _ in range(int(input()))]
    
    for c in contacts:
        result = email.utils.parseaddr(c)
        if is_valid_email(result[1]):
            result = email.utils.formataddr(result)
            print(result)