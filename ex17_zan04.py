
if __name__ == '__main__':
    # 2 + 4 + ... + 98 + 100 = 2550
    i = 1
    sum_n = 0
    is_completed = False

    while i <= 100: 
        i += 1

        if i == 5:
            break
        
        sum_n += i  
    else:
        is_completed = True

    print(f'2 + 4 + ... + 98 + 100 = {sum_n} is completed:{is_completed}')
    print('---')