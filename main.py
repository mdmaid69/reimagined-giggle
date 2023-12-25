import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"