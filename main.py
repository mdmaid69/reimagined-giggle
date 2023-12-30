import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)