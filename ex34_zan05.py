def show(title, ver='1.2.1', *args, **kwargs):

    print(f'positional (title):{title}')

    print(f'optional (ver):{ver}')

    print('args:')
    for i in args:
        print(f'{i}', end=' ')
    print()

    if 'color' in kwargs:
        print(f'kwargs:{kwargs["color"]}')
    if 'font' in kwargs:
        print(f'kwargs:{kwargs["font"]}')
    if 'align' in kwargs:
        print(f'kwargs:{kwargs["align"]}')

    print('-- end --')

if __name__ == '__main__':
    # 1
    # show('Text Editor')

    # 2
    # show('Text Editor', '1.3.2')

    # 3
    # show('Text Editor', '1.3.2', 5, 4, 7, 8)

    show('Text Editor', '1.3.2', 5, 4, 7, 8, font='monospace', color='red')

    conf = {
        'font':'sans-serif',
        'size':10,
        'color':'black',
        'padding':5,
        'align': 'left'
    }

    show('Text Editor', '1.3.2', 5, 4, 7, 8, **conf)
    
    print('---')