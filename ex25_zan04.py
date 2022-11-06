
if __name__ == '__main__':
    
    conn = {
        'host':'localhost',
        'port':1521,
        'alt_hosts':['server1.com', 'server2.com', 'db-app.com'],
        'db':'northwind',
        'service':'oracle'
    }

    for item in conn.items():
        key, value = item

        if type(value) is list:
            continue
        
        print(f'{key} => {value}')

    print('---')