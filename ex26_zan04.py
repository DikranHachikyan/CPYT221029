
if __name__ == '__main__':
    
    sq = [  v ** 2 for v in range(1,11)]

    print(f'values:{sq}')

    txt = 'Lorem ipsum dolor sit amet'

    symbs = [ f'-{t}-'.upper() for t in txt]

    print(f'symbs:{symbs}')


    print('---')