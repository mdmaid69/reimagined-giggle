def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)