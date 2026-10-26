# Week 1.5, Session 1: Task 3

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def__init__(self, x_coordinate, y_coordinate):
       self.x = x_coordinate
       self.y = y_coordinate
    # Add distance() method here
    def distance (self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    # Add distance_to() method here
    def distance_to(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return (dx ** 2 + dy ** 2) ** 0.5
    # (This will need a parameter representing another point)
p1 = Point(3, 4)
p2 = Point(6, 8)

print(p1.distance())
print(p1.distance_to(p2))




# Finally, add code here to demonstrate use of Point
