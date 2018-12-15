import structshape
import math


class point(object):
    '''Represent a point in 2D space
    which has x cor <f> and y cor <f>
    can be show with showCor method'''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def showCor(self):
        print('(%f , %f)'%(self.x,self.y))


def distance_bw_2point(A, B):
    '''Calculate distance of 2 point A <point> and B <point>'''
    return math.sqrt((A.x - B.x) ** 2 + (A.y - B.y) ** 2)

if __name__=='__main__':
    PointA = point(3, 4)
    PointB = point(4, 8)
    PointA.showCor()
    PointB.showCor()
    print(distance_bw_2point(PointA, PointB))
