#Jason Guan
#U9893-2926
#Program intended to promot the user for number of sides and lengths to
#calcuate the perimeter and area of the polygon

import math
class Polygon_Math:
    def __int__(self, s=0, l=0.0):
        self.__sides = s
        self.__length = l
    def setSides(self, s):
        self.__sides = s
    def setLength(self, l):
        self.__length = l
    def getSides(self):
        return self.__sides
    def getLength(self):
        return self.__length
    def perimeter(self):
        return self.__sides * self.__length
    def area(self):
        a = (self.__sides * self.__length * self.__length) / (4 * math.tan(math.pi / self.__sides))
        return a

def main():
    p = Polygon_Math()
    sides = int(input("Enter the number of sided (>=3): "))
    while True:
        if(sides < 3):
           sides = int(input("Invalid entry. Re-enter the number of sides (>=3)"))
        else:
            break

    p.setSides(sides)

    length = float(input("Enter the length of each sides (>=0.1): "))
    while True:
        if(length < 0.1):
          length = float(input("Invalid entry. Re-enter the length of each sides (>=0.1): "))
        else:
            break

    p.setLength(length)
    p.setSides(sides)
    print("The polygon has", p.getSides(), "sides. Each sides is", p.getLength(), "units in length.")
    print("The perimeter of the polygon is {:.3f} units and its area is {:.3f} square units.".format(p.perimeter(), p.area()))

main()
