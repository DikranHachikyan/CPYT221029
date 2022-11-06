# port - глобална променлива
port = 3306
# 1. дефиниция
def sum_numbers(a, b, *args):
    '''Sum values'''
    # тяло на функцията
    # c - локална променлива
    c = a + b
    # print(f'args:{args} type is:{type(args)}')
    for v in args:
        c += v
    return c

if __name__ == '__main__':
    
    # 2. извикване
    res1 = sum_numbers(5,6)

    x, y, z = 10, 20, 5
    res2 = sum_numbers(x, y, z, 22)
    
    res3 = sum_numbers(x, y ** 2)

    arr = [1,2,3,4]

    res4 = sum_numbers(x, y, *arr)

    print(f'res1={res1} res2={res2} res3={res3} res4={res4}')
    print('---')