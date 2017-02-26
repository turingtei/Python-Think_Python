"""
Objects are mutable
"""
"""
Instances as return values

"""

class Rectangle(object):
  """Represents a rectangle.

  attributes: width, height, corner.
  """
class Point(object):
  """Represents a point in 2-D space."""

box = Rectangle()
box.width = 100.0
box.height = 200.0

box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def find_center(rect):
  p = Point()
  p.x = rect.corner.x + rect.width / 2.0
  p.y = rect.corner.y + rect.height / 2.0
  return p

def print_point(p):
  print ('(%g, %g)' % (p.x, p.y))

center = find_center(box)
print_point(center)

"""
Can change the state of an object by making an
assignment to one of its attributes
"""
box.width = box.width + 50
box.height = box.height + 50

"""
Can write functions that modify objects.
grow_rectangle takes a rectangle object and
two numbers, dwidth and dheigh, and adds the
numbers to the width and height of the 
rectangle
"""

def grow_rectangle(rect, dwidth, dheight):
  rect.width += dwidth
  rect.height += dheight

print (box.width)
print (box.height)
grow_rectangle(box,50,100)
print (box.width)
print (box.height)
