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
time = Time()
time.hour = 11
time.minute = 59
time.second = 30

print_time(time)

