import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"