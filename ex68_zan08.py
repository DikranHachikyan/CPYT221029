# 1. дефиниция на класа
# 
class Point:

    def __init__(self, *, x=0, y=0, **kwargs):
        print('-- init point --')
        # данни на обекта
        self.x = x
        self.y = y 
    
    # методи на обекта

    def draw(self):
        print(f'draw point at ({self.x}, {self.y})')

    def move_to(self, dx, dy):
        self.x += dx
        self.y += dy

    # методи за достъп до данните
    @property
    def x(self):
        # get method
        return self.__x
    
    @x.setter
    def x(self, x):
        # set method
        assert isinstance(x,(int,float)) and x >= 0 and x <= 1000, 'invalid value for x'
        self.__x = x
    
    @property
    def y(self):
        # get method
        return self.__y
    
    @y.setter
    def y(self, y):
        # set method
        assert isinstance(y,(int,float)) and y >= 0 and y <= 1000, 'invalid value for y'
        self.__y = y
    

        



if __name__ == '__main__':
    # 2. декларация на променлива от типа
    # клас - типът, Point; обект - представител на класа, p
    print('--- begin ---')
    p1 = Point(x=10, y=20)
    p2 = Point()

    p2.x = 20
    p2.y = 11
    p2.draw()
    p2.move_to(44,55)
    p2.draw()

    print('--- end ---')