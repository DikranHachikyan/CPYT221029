# 1. дефиниция на класа
# 
class Point:

    def __init__(self, *, x=0, y=0, **kwargs):
        print('-- init point --')
        # данни на обекта
        self.__x = x
        self.__y = y 
    
    # методи на обекта

    def draw(self):
        print(f'draw point at ({self.__x}, {self.__y})')

    def move_to(self, dx, dy):
        self.__x += dx
        self.__y += dy

if __name__ == '__main__':
    # 2. декларация на променлива от типа
    # клас - типът, Point; обект - представител на класа, p
    print('--- begin ---')
    p1 = Point(x=10, y=20)
    
    # p1.x = -1000

    # AttributeError: 'Point' object has no attribute '__x'
    # print(f'point x={p1.__x}')

    p1.draw()
    
    
    print('--- end ---')