  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)