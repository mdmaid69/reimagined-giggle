  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)