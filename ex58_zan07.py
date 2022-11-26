
# 2. прилагаме декоратора

if __name__ == '__main__':

    actions = {
        '+': lambda a, b: a + b
    }
    op = ''
    value1, value2, result = 0, 0, 0

    while True:
        try:
            op = input('action (+, q-quit):')
            if op == 'q':
                break

            value1 = float(input('first value:'))
            value2 = float(input('second value:'))

            result = actions[op](value1, value2)
        except KeyError as e:
            print(f'Unsupported operation ({op}) [Key Error:{e}]')
        except ValueError as e:
            print(f'Invalid number [Value Error:{e}]')
        except Exception as e:
            print(f'Unknown Error!{e}')
        else:
            print(f'{value1} {op} {value2} = {result}')
        finally:
            print('-- finally --')

    print('---')