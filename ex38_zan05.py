def show(title, *, ver='1.2.1', margin,**kwargs):

    print(f'positional (title):{title}')


    print(f'keyword-only (ver):{ver} (margin):{margin}')
    
    settings = {
        'color': kwargs.get('color','blue'),
        'font':  kwargs.get('font','serif'),
        'align': kwargs.get('align', 'center')
    }
    
    print(f'kwargs:{settings}')

    print('-- end --')

if __name__ == '__main__':


    show('Text Editor',margin=10)
    
    show('Text Editor', margin=15, ver='1.3.2',  font='monospace', color='red')

    conf = {
        'font':'sans-serif',
        'size':10,
        'color':'black',
        'padding':5,
        'align': 'left'
    }

    show('Text Editor', margin=1, **conf)
    
    print('---')