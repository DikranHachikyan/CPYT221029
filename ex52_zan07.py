# 1.
# import time
# print(f'time:{time.time()}')

# 1.1
# import time as tm
# print(f'time:{tm.time()}')

# 2. 
# from time import time
# print(f'time:{time()}')

# 2.1
# from time import time as now
# print(f'time:{now()}')

# 2.2
# from time import time as now, sleep
from time import time, sleep
from functools import wraps
# 1. дефинираме декоратора

def to_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args = [ f'{v}' for v in args]
        return func(*args, **kwargs)
    return wrapper

def add_brackets(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args = [ f'[{v}]'  for v in args]
        return func(*args, **kwargs)
    return wrapper    

# 2. прилагаме декоратора
@add_brackets
@to_string
def concat(*args, **kwargs):
    '''Concatenate args with separator sep'''
    sep = kwargs.get('sep', ';')
    return sep.join(args)

if __name__ == '__main__':
    users = ['anna','maria','markus','jorg']

    print( concat(*users, sep='|'))
    print( concat(*users))
   
    values = [10,20,30,40,50]

    print(concat( *values, sep=':'))

    print('---')