"""
Modifiers

a function modifies the objects it gets as parameters
the changes are visible to the caller

"""
def increment(time, seconds):
  time.second += seconds

  if time.second >= 60:
    time.second -= 60
    time.minute += 1

  if time.minute >= 60:
    time.minute -= 60
    time.hour += 1
