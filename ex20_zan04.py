
if __name__ == '__main__':
    tpl = 12, 23, 45, 67, 78

    for item in enumerate(tpl, start=6):
        idx, value = item
        print(f'idx = {idx}, value = {value}')
        
    print('---')