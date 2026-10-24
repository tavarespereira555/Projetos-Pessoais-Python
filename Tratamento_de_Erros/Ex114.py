from urllib.error import URLError

import requests
try:
    resp= requests.get('https://pudim.com.br/', timeout=5)
except URLError:
    print('\033[31mO site do pudim não esta acessivel no momento\033[m')
else:
    print('\033[34mO site do pudim esta acessivel no momento\033[m')