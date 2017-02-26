"""
Copying
an alternative to aliasing
the copy module contains a function 'copy'
that duplicates any object
"""
"""
Write a function named 'move_rectangle'
that takes a rectangle and two numbers
'dx' and 'dy'

Change the location of the rectangle by adding
'dx' to the x coordinate of corner and adding
'dy' to the y coordinate of corner.
"""
import copy

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

box.width = box.width + 50
box.height = box.height + 50


def grow_rectangle(rect, dwidth, dheight):
  rect.width += dwidth
  rect.height += dheight

def move_rectangle(rect,dx,dy):
  rect.corner.x += dx
  rect.corner.y +=dy

print (box.corner.x)
print (box.corner.y)
move_rectangle(box,10,20)
print (box.corner.x)
print (box.corner.y)

p1 = Point()
p1.x = 3.0
p1.y = 4.0

p2 = copy.copy(p1)
"""p1 and p2 contain the same data but they
are not the same 'Point'
"""

box2 = copy.copy(box)
box2 is box #False
box2.corner is box.corner   #True

"""
shallow copy, it copies the object and any
references it contains, but not the embedded objects

grow_rectangle would not affect both
more_rectangle would affect both
"""

""""
Deep copy
"""

box3 = copy.deepcopy(box)
box3 is box  #False
box3.corner is box.corner #False


