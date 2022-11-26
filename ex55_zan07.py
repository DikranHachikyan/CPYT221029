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

if __name__ == '__main__':

    print('hello', 'python','c++','java')

    print = to_upper(print) 
    
    print('hello', 'python','c++','java')

    print = print.__original

    print('hello', 'python','c++','java')
   
    print('---')