def print_key(key, **kwargs):
    try:
        print(f'{key} => {kwargs[key]}')
    except KeyError as e:
        raise
        # 2. крайно лоша идея
        # pass

        # 1. не е добра идея така да правим
        # print(f'invalid key {key}')

if __name__ == '__main__':

    conn = {
        'host':'localhost',
        'port':1521,
        'db':'northwind'
    }

    try:
        print_key('host', **conn)
        print_key('ip', **conn)
    except KeyError as e:
        print(f'invalid key {e}')
        
    print('---')