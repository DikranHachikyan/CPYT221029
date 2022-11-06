# port - глобална променлива
port = 3306
# 1. дефиниция
def sum_numbers(a, b, d=0):
    # тяло на функцията
    # c - локална променлива
    c = a + b + d

    return c

if __name__ == '__main__':
    
    # 2. извикване
    res1 = sum_numbers(5,6)

    x, y, z = 10, 20, 5
    res2 = sum_numbers(x, y, z)
    
    res3 = sum_numbers(x, y ** 2)

    print(f'res1={res1} res2={res2} res3={res3}')
    print('---')