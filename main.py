  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
def calculate_roi(gain, cost):
        return (gain - cost) / cost