import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"