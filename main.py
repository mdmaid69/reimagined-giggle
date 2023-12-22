  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import math
def calculate_combinations(n, k):
        return math.comb(n, k)