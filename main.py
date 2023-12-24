  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
def calculate_pressure(force, area):
        return force / area