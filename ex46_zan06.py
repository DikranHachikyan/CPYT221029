# def foo(n):
#     return n * 10

if __name__ == '__main__':

    pow_xy = lambda x, y: x ** y

    z = pow_xy(3, 4)
    print(f'z={z}')

    numbers = [3, 5, 6, 7, 4]

    for i  in map(lambda el: el * 10, numbers):
    # for i  in map(foo, numbers):
        print(f'i = {i}')

    print('---')