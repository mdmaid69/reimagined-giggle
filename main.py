import re
def split_string(pattern, string):
        return re.split(pattern, string)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)