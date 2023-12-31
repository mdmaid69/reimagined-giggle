import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)