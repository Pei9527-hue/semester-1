# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

class Point:
    """
    A Point in 2D space.

 def__init__(self, x_coordinate, y_coordinate):
       self.x = x_coordinate
       self.y = y_coordinate
    """
class Circle:
  """A circle in 2D space."""
  def __int__(self, centre, radius):
    self.centre = centre
    self.radius = radius

  def area(self):
    """Return the area of the circle."""
       reyurn math.pi * self.radius ** 2

  def perimeter(self):
    """Return the perimeter of the circle."""
    return 2 * math.pi * self.radius

   
   

# Copy Point class definition here

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

# Don't add any testing code to this file!
