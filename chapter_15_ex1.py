"""
Write a function called distance_between_points
that takes two points as arguments and returns
the distance between them

"""
import math

class Point(object):
  """something"""

pointA = Point()
pointA.x = 2
pointA.y = 4

pointB = Point()
pointB.x = 5
pointB.y = 2

def distance_between_points(a,b):
  distance = math.sqrt(((a.x-b.x)**2)+((a.y-b.y)**2))
  print (distance)

distance_between_points(pointA,pointB)