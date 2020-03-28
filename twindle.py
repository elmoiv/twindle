# requests.head checks headers only
# without downloading the whole page
from requests import head
from random import choice
from colorama import Fore, Style, init

# Colorama module's initialization.
init(autoreset=True)

BASEURL = 'https://mobile.twitter.com/'
CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789_'
STATE = {
    404: ('Free', Fore.LIGHTGREEN_EX),
    307: ('Suspended', Fore.RED),
    200: ('Active', Fore.LIGHTMAGENTA_EX)
    }
DATA = []

def test_handle(h):
    global DATA
    st = head(BASEURL + h).status_code
    if st == 404:
        # Avoid duplicates
        if not h in DATA:
            DATA.append(h)
    return STATE[st]

def run(test_len):
    l = int(input('Enter handle length: '))
    if not l:
        raise ValueError('Handle can not be empty')
    if not 4 < l < 16:
        raise ValueError('Handle must be > 4 and < 16')
    
    print()

    for i in range(1, test_len + 1):
        handle = ''.join(choice(CHARS) for i in range(l))
        
        print(
            Fore.WHITE + f'[{i}]'.ljust(5) + 'Trying: ' +
            Fore.YELLOW + handle + Fore.WHITE + ' - Result: '
            + Style.BRIGHT, end = ''
            )
        
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
