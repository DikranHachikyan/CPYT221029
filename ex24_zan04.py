
if __name__ == '__main__':
    
    conn = {
        'host':'localhost',
        'port':1521,
        'db':'northwind',
        'service':'oracle',
        'alt_hosts':['server1.com', 'server2.com', 'db-app.com']
    }

    for item in conn.items():
        key, value = item

        print(f'{key} => {value}')

    print('---')