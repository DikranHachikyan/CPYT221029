from time import time, sleep
from functools import wraps
# 1. дефинираме декоратора

def to_upper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.__original = func
        args = [ f'{v}'.upper() for v in args]
        return func(*args, **kwargs)
    return wrapper

# 2. прилагаме декоратора
@to_upper
def concat(*args, **kwargs):
    '''Concatenate args with separator sep'''
    sep = kwargs.get('sep', ';')
    return sep.join(args)

if __name__ == '__main__':
    users = ['anna','maria','markus','jorg']
    values = [10,20,30,40,50]

    print( concat(*users, sep='|') )
    print( concat( *values, sep=':') )

    # 1. временно използваме първоначалния вариант
    print(concat.__original(*users))

    # 2. премахваме декоратора
    concat = concat.__original
    print( concat(*users) )
   


    print('---')