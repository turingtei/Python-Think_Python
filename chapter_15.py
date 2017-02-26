import math

class Point(object):
  """Represents a point in 2-D space."""

print (Point)
blank = Point()
print (blank) #what class it belogs to and where is stored in memory

#15.2 Attributes
blank.x = 3.0
blank.y = 4.0

print (blank.y)
x = blank.x
print (x)

print ('(%g, %g)' % (blank.x, blank.y))
distance = math.sqrt(blank.x**2 + blank.y**2)
print (distance)

def print_point(p):
  print ('(%g, %g)' % (p.x, p.y))

print_point(blank)