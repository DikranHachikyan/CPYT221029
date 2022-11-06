
if __name__ == '__main__':
    
    # for i in range(3):
    #     for j in range(4):
    #         print(f'i={i} j={j}')

    values = [ f'i={i} j={j}' for i in range(3) for j in range(4)]
    print(f'values={values}')

    print('---')