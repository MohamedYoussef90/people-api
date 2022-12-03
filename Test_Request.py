import requests
from pprint import pprint

def new_func():
    return "https://api.github.com/events"



def pretty_print(msg, indent=2):
    print()
    pprint(msg,indent=indent)

responce = requests.get(new_func())
turn = responce.json()
pretty_print (turn)

# payload = {'key1': 'value1', 'key2': 'value2','Key3' : 'Value3'}
# r = requests.get('https://httpbin.org/get', params=payload)
# print(r.text)

# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

# r = requests.get('https://httpbin.org/get', params=payload)
# print(r.text)
