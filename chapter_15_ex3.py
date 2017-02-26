"""
Write a function named 'move_rectangle'
that takes a rectangle and two numbers
'dx' and 'dy'

Change the location of the rectangle by adding
'dx' to the x coordinate of corner and adding
'dy' to the y coordinate of corner.
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

box.width = box.width + 50
box.height = box.height + 50


def grow_rectangle(rect, dwidth, dheight):
  rect.width += dwidth
  rect.height += dheight

def move_rectangle(rect,dx,dy):
  rect.corner.x += dx
  rect.corner.y +=dy

def move_rectangle_copy(rect,dx,dy):
  new = copy.deepcopy(rect)
  move_rectangle(new,dx,dy)
  return new

print (box.corner.x)
print (box.corner.y)
move_rectangle(box,10,20)
print (box.corner.x)
print (box.corner.y)