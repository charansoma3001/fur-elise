import math

class distanceBW2points():
    '''rep'''

point1=distanceBW2points()
point2=distanceBW2points()

point1.x1=4.0
point1.y1=5.0

point2.x2=12.0
point2.y2=14.0

print(math.sqrt((point2.x2 - point1.x1)**2) + (point2.y2-point1.y1)**2)
