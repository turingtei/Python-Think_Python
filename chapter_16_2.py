"""
Pure functions
"""
class Time(object):
  """Represents the time of day.

  attributes: hour, minute, second
  """

  #create a new Time object and assign attributes

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

def add_time(t1,t2):
  sum = Time()
  sum.hour = t1.hour + t2.hour
  sum.minute = t1.minute + t2.minute
  sum.second = t1.second + t2.second

  if sum.second >= 60:
    sum.second -= 60
    sum.minute += 1
  if sum.minute >= 60:
    sum.minute -= 60
    sum.hour += 1
    
  return sum

def print_time(object):
  print("%.2d : %.2d : %.2d" % (object.hour, object.minute, object.second))

start = Time()
start.hour = 9
start.minute = 45
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

done = add_time(start,duration)
print_time(done)