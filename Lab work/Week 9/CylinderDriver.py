from Cylinder import Cylinder
x = Cylinder("a")
Radius = int(input("Enter Radius: "))
while Radius <= 0:
    print("Radius cannot be equal to or less than 0")
    Radius = float(input("Please, Re-enter Radius:"))
x.setRadius(Radius)
print("the Radius is:", x.getRadius())
x.setColor(input("Enter Color: "))
print("The Color is:", x.getColor())
x.setheight(float(input("Enter height: ")))
print("The height is:", x.getheight())
print("and the volume is:", x.getvolume())
print(x.__str__())