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
def measure_time(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        t = time()
        func(*args, **kwargs)
        out = f'{func.__name__} exec time:{time() - t:.3f} s (doc:{func.__doc__})'
        print(out)
    return wrapper

# 2. прилагаме декоратора
@measure_time
def foo(sleep_time=0.5):
    '''function foo, sleeps sleep_time seconds'''
    sleep(sleep_time)


if __name__ == '__main__':

    foo()

    foo(0.2)

    print(f'name:{foo.__name__} doc:{foo.__doc__}')

    print('---')