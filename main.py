import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)