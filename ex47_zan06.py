
if __name__ == '__main__':

    options = {
        '+': lambda a, b: a + b
    }

    ch = input('Actions (+,q-quit):')

    if ch == 'q':
        quit()
    if ch in '+':
        n1 = float(input('n1='))
        n2 = float(input('n2='))
        res = options[ch](n1,n2)
        print(f'{n1} {ch} {n2} = {res}')

    print('---')