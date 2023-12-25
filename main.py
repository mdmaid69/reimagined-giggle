import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"