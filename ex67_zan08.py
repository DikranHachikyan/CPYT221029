# 1. дефиниция на класа
# 
class Point:

    def __init__(self, *, x=0, y=0, **kwargs):
        print('-- init point --')
        # данни на обекта
        self.set_x(x)
        self.set_y(y) 
    
    # методи на обекта

    def draw(self):
        print(f'draw point at ({self.get_x()}, {self.get_y()})')

    def move_to(self, dx, dy):
        self.set_x( self.get_x() + dx)
        self.set_y( self.get_y() + dy)

    # методи за достъп до данните
    def set_x(self, x):
        assert isinstance(x,(int,float)) and x >= 0 and x <= 1000, 'invalid value for x'
        self.__x = x

    def get_x(self):
        return self.__x

    def set_y(self, y):
        assert isinstance(y,(int,float)) and y >= 0 and y <= 1000, 'invalid value for y'
        self.__y = y

    def get_y(self):
        return self.__y

        



if __name__ == '__main__':
    # 2. декларация на променлива от типа
    # клас - типът, Point; обект - представител на класа, p
    print('--- begin ---')
    p1 = Point(x=10, y=20)
    p2 = Point()

    p2.set_x(20)
    p2.draw()
    p2.move_to(11,22)
    p2.draw()

    # p2.set_x('1')

    print('--- end ---')