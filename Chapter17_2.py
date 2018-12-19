class Point(object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return ('x= %.2f ; y= %.2f'%(self.x,self.y))
    def __add__(self,other):
        assert isinstance(other,Point) or isinstance(other,tuple),'Second input parameter is not valid \n it must be a Poin object or a Tuple'
        if isinstance(other,Point)==True:
            tmpPoint=Point()
            tmpPoint.x=self.x+other.x
            tmpPoint.y=self.y+other.y
            return tmpPoint
        else:
            tmpPoint = Point()
            tmpPoint.x = self.x + other[0]
            tmpPoint.y = self.y + other[1]
            return tmpPoint
    def __radd__(self, other):
        return self.__add__(other)
    def print_attributes(self):
        for attr in self.__dict__:
            print(attr, getattr(self, attr))
if __name__=='__main__':
    A=Point()
    B=Point(2)
    C=Point(0,3)
    D=Point(2.5,3.4)
    E=C+D
    print(C,'\n',D,'\n',E)
    print(E is C)
    E=C+D
    print(C,'\n',D,'\n',E)
    F=C+(4,5)
    print(F)
    G=(6,7)+C
    print(G)
    print(G.__dict__)
    G.print_attributes()
