class NameNotFoundError(Exception):
    pass

def print_key(key, **kwargs):
    
    if key not in kwargs:
        raise NameNotFoundError(f'Please, check .... {key}' )
    
    print(f'{key} => {kwargs[key]}')
    

if __name__ == '__main__':

    conn = {
        'host':'localhost',
        'port':1521,
        'db':'northwind'
    }

    try:
        print_key('host', **conn)
        print_key('ip', **conn)
    except NameNotFoundError as e:
        print(f'invalid key {e}')
        
    print('---')