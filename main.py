  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)