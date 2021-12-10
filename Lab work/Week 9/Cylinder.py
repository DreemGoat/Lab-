import math
class Circle:
    def __init__(self,radius=1,color=""):
        self.radius = radius
        self.color = color
        
    def setRadius(self,radius):
        if radius > 0:
            self.radius = radius
        else:
            radius = 1

    def setColor(self,color):
        self.color = color
    
    def getRadius(self):
        return self.radius

    def getColor(self):
        return self.color

    def getArea(self):
        return math.pi * self.getRadius()**2

    def __str__(self):
        return "Radius= {:.2f}". format(self.getRadius()) + \
            "Color =", self.getColor()

class Cylinder(Circle):
    def setheight(self, height):
        self.height = height

    def getheight(self):
        return self.height

    def getvolume(self):
        return self.getArea() * self.getheight()

    def __str__(self):
        return "Radius= {:.2f}". format(self.getRadius()) + \
            "Color =", self.getColor() +\
            "Height ={:.2f}". format(self.getheight())