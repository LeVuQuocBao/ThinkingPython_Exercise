from structshape import structshape
class Container(object):
    def __init__(self):
        self.box_contents=[]
    def put_in_box(self,obj):
        self.box_contents.append(obj)
    def __str__(self):
        return (str(self.box_contents))
TruckA=Container()
Thing1='Table'
Thing2=2
Thing3=(3,4)
Thing4=[3,4]
TruckA.put_in_box(Thing1)
TruckA.put_in_box(Thing2)
TruckA.put_in_box(Thing3)
TruckA.put_in_box(Thing4)
TruckB=Container()
TruckB.put_in_box(TruckA)
print(TruckA)
print(TruckB)
print(TruckB.box_contents[0]is TruckA)