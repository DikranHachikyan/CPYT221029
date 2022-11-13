def get_squares(n):
    return [ v ** 2 for v in range(1, n+1)]

# 1. дефиниция
def gen_squares(n):

    for v in range(1,n+1):
        yield v ** 2

if __name__ == '__main__':

    values = get_squares(10)
    print(f'values={values}')
    
    # 2. присвояваме генератора на променлива

    gs = gen_squares(10)

    print(f'types: generate_squares is {type(gen_squares)} gs is {type(gs)}')

    # 3. консумиране на генератора
    print(f'1 => {next(gs)}')
    print(f'2 => {next(gs)}')
    print(f'3 => {next(gs)}')
    print(f'4 => {next(gs)}')

    arr2 = list(gs)
    print(f'arr2 = {arr2}')
    
    # StopIteration 
    # print(f'after last element => {next(gs)}')
    
    gs2 = gen_squares(4)

    for v in gs2:
        print(f'v={v}')
        
    print('---')