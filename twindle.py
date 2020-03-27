from requests import head
from random import choice
from colorama import Fore, Style, init

# Colorama module's initialization.
init(autoreset=True)

BASEURL = 'https://mobile.twitter.com/'
CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789_'
LENGTH = 15
STATE = {404: ('Free', Fore.LIGHTGREEN_EX),
        307: ('Suspended', Fore.RED),
        200: ('Active', Fore.LIGHTMAGENTA_EX)}
DATA = []

def test_handle(h):
    global DATA
    st = head(BASEURL + h).status_code
    if st == 404:
        if not h in DATA:
            DATA.append(h)
    return STATE[st]

def run(test_len):
    l = int(input('Enter handle length (<= 15): '))
    if l > LENGTH or not l:
        raise ValueError('Handle cannot be empty or longer than 15 characters')
    
    print()

    for i in range(1, test_len + 1):
        handle = ''.join(choice(CHARS) for i in range(l))
        
        print(Fore.WHITE + f'[{i}]'.ljust(5) + 'Trying: ' + Fore.YELLOW + handle + Fore.WHITE + ' - Result: ' + Style.BRIGHT, end = '')
        
        st, color = test_handle(handle)
        print(color + st)

    print('\nDone!')

def store_free():
    with open('free_handles.txt', 'w') as storedb:
        storedb.write('\n'.join(DATA))

if __name__ == '__main__':
    run(int(input('TEST COUNT: ')))
    store_free()
    input(f'Free Handles: {len(DATA)}')