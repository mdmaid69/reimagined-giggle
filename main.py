  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)