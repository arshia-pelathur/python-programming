from points_on_plane import Point

class traingle:
    def __init__(self,point1,point2,point3):
        self.__vertices = [point1,point2,point3]
        self.__perimeter = None
    def perimeter(self):
        a = self.__vertices[0].distance_point(self.__vertices[1])
        b = self.__vertices[1].distance_point(self.__vertices[2])
        c = self.__vertices[2].distance_point(self.__vertices[0])
        self.__perimeter = a + b + c
    
    def __str__(self):
        return f'The perimeter of the traingle is {self.__perimeter}'

tr = traingle(Point(0,0),Point(1,0),Point(0,1))
tr.perimeter()
print(tr)