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
    # ----------------
    # специални методи
    # Предефиниране на метод (Function Overriding)
    #
    def __str__(self):
        return f'({self.x},{self.y})'

    def __eq__(self,other):
        if not isinstance(other, Point):
            raise NotImplementedError('Not implemented yet')
        # self.x, self.y - ЛО, p1
        # other.x, other.y - ДО, p3
        return self.x == other.x and self.y == other.y
        
    def __add__(self, other):
        new_x, new_y = 0,0
        if isinstance(other, Point):
            new_x = self.x + other.x
            new_y = self.y + other.y
        elif isinstance(other, (int,float)):
            new_x = self.x + other
            new_y = self.y + other
        else:
            raise NotImplemented('Not yet implementer')    

        return Point(x=new_x, y=new_y)


if __name__ == '__main__':
    pass