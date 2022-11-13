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

def foo():
    sleep(0.5)

def bar():
    sleep(0.3)

if __name__ == '__main__':

    t = time()
    foo()
    print(f'foo execution time:{time() - t:.3f}s')

    t = time()
    bar()
    print(f'bar execution time:{time() - t:.3f}s')
        
    print('---')