  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
  def calculate_perimeter_triangle(a, b, c):
        return a + b + c