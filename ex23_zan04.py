
if __name__ == '__main__':
    
    conn = {
        'host':'localhost',
        'port':1521,
        'db':'northwind',
        'service':'oracle',
        'alt_hosts':['server1.com', 'server2.com', 'db-app.com']
    }

    for key in conn:
        print(f'key:{key} => {conn[key]}')

        if type(conn[key]) is list:
            for value in conn[key]:
                print(f'  value:{value}')

    print('---')