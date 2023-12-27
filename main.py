  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height