# 1 + 2 + 3 + .... + 99 + 100 + ... + n

def sum_n(n):
    print(f'n={n}')
    if n > 0:
        return n + sum_n(n-1)
    return 0

if __name__ == '__main__':
    val = 5

    res = sum_n( val )
    
    print(f'1 + ... + {val}={res}')
    
    print('---')