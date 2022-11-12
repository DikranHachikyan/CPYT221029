def show(title, ver='1.2.1', *args, **kwargs):

    print(f'positional (title):{title}')

    print(f'optional (ver):{ver}')

    print('args:')
    for i in args:
        print(f'{i}', end=' ')
    print()

    settings = {
        'color': kwargs.get('color','blue'),
        'font':  kwargs.get('font','serif'),
        'align': kwargs.get('align', 'center')
    }
    
    print(f'kwargs:{settings}')

    print('-- end --')

if __name__ == '__main__':


    show('Text Editor')
    
    show('Text Editor', '1.3.2', 5, 4, 7, 8, font='monospace', color='red')

    conf = {
        'font':'sans-serif',
        'size':10,
        'color':'black',
        'padding':5,
        'align': 'left'
    }

    show('Text Editor', 5, 4, 7, 8, **conf)
    
    print('---')