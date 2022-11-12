# глобална променлива
port = 1521

def show():
    global port
    port = 3306
    print(f'local value - port={port}')

if __name__ == '__main__':

    print(f'before - port={port}')
    show()
    print(f'after - port={port}')
    print('---')