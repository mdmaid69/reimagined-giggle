import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)