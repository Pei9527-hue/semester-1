# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class
from geometry import Point, Circle
circle = Circle(9)

p1 = Point(4,3)
p2 = Point(7,8)
p3 = Point(9,1)

print (p1 in circle)
print (p2 in circle)
print (p3 in circle)