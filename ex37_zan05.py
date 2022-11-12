def show(title,  *args, ver='1.2.1', **kwargs):

    print(f'positional (title):{title}')

    print('args:')
    for i in args:
        print(f'{i}', end=' ')
    print()

    print(f'keyword-only (ver):{ver}')
    
    settings = {
        'color': kwargs.get('color','blue'),
        'font':  kwargs.get('font','serif'),
        'align': kwargs.get('align', 'center')
    }
    
    print(f'kwargs:{settings}')

    print('-- end --')

if __name__ == '__main__':


    show('Text Editor')
    
    show('Text Editor', 5, 4, 7, 8, ver='1.3.2', font='monospace', color='red')

    conf = {
        'font':'sans-serif',
        'size':10,
        'color':'black',
        'padding':5,
        'align': 'left'
    }

    show('Text Editor', 5, 4, 7, 8, **conf)
    
    print('---')