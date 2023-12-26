  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
def calculate_area_circle(r):
        return 3.14 * r**2