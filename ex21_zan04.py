
if __name__ == '__main__':
    tpl = 12, 23, 45, 67, 78
    n = len(tpl)

    # for idx in range(1,n,2):
    for idx in range(n):
        print(f'idx={idx} value={tpl[idx]}')
        
    print('---')