  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)