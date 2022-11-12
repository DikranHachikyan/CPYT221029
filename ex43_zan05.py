def foo(a=[], b={}):
    print(f'a={a}')
    print(f'b={b}')

    n = len(a)
    a.append(n)
    b[n] = n
    print('--- end foo ---')


if __name__ == '__main__':
    
    foo()

    foo([4,5,6], {'z':10})

    foo()

    foo([41,15,16,10], {'z':10, 's':4})

    foo()
    foo()
    print('---')