"""
Write a boolean function 'is_after'
that takes two Time objects, t1 and t2,
and returns True if t1 follows t2 chronologically
and False otherwiese.

Challenge: don't us an if statement

"""

"""
Time
"""

class Time(object):
  """Represents the time of day.

  attributes: hour, minute, second
  """

  #create a new Time object and assign attributes
def print_time(object):
  print("%.2d : %.2d : %.2d" % (object.hour, object.minute, object.second))

def is_after(a,b):
  return (a.hour, a.minute, a.second) > (b.hour, b.minute, b.second)

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

print_time(time)

t1 = Time()
t1.hour = 2
t1.minute = 0
t1.second = 0
t2 = Time()
t2.hour = 5
t2.minute = 0
t2.second = 0
print (is_after(t1,t2))