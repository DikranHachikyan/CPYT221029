def foo(values, n):
    n = n ** 2
    print(f'local value of n:{n}')
    
    values.sort()

if __name__ == '__main__':
    # mutable
    numbers = [5, 4, 6, 3, 7, 9, 8]
    # immutable
    a = 10

    print(f'before numbers:{numbers} a={a}')
    foo(numbers, a)
    print(f'after numbers:{numbers} a={a}')
    print('---')