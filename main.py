  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))