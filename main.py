def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)