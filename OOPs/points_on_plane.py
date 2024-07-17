import numpy as np


class Point:

    def __init__(self,x=0,y=0):
        self.__x = float(x)
        self.__y = float(y)

    def getx(self):
        return self.__x
    
    def gety(self):
        return self.__y
    
    def distance_from_xy(self,x,y):
        return np.sqrt((x-self.__x)**2 + (y-self.__y)**2)
        
    def distance_point(self,point):
        return self.distance_from_xy(point.getx(),point.gety())
    

p1 = Point(0,0)
p2 = Point(2,2)
print(p1.distance_from_xy(2,0))
print(p1.distance_point(p2))
