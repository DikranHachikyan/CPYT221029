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

if __name__ == '__main__':
    # 2. декларация на променлива от типа
    # клас - типът, Point; обект - представител на класа, p
    print('--- begin ---')
    p1 = Point()
    p2 = Point(x=20, y=30)

    p1.draw()
    p2.draw()

    p1.move_to(10,15)
    p1.draw()
    
    print('--- end ---')