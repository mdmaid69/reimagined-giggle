  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import re
def split_string(pattern, string):
        return re.split(pattern, string)