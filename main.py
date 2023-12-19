  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
def calculate_density(mass, volume):
        return mass / volume