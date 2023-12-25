import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"