import requests
from getpass import getpass

payload = {'username': 'bob', 'email': 'bob@bob.com'}

try:
    response = requests.patch(auth=('prasadnaddy',getpass()),url="https://api.github.com/user",data=payload)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(e)
    raise