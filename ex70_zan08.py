from draw.point import Point

if __name__ == '__main__':
    # 2. декларация на променлива от типа
    # клас - типът, Point; обект - представител на класа, p
    print('--- begin ---')
    p1 = Point(x=10, y=20)
    p2 = Point()
    p3 = Point(x=10, y=20)

    print(f'Point p1:{p1}, p3:{p3}')
    # txt = str(p1)
    # print(txt)
    # p4 = p3
    if p1 == p3:
        print(f'{p1} equals {p3}')
    else:
        print(f'{p1} not equals {p3}')

    p4 = p1 + p3
    print(f'p4:{p4}')

    p4 = p1 + 10.0
    print(f'p4:{p4}')
    print('--- end ---')