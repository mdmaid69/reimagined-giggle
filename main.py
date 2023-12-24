  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)