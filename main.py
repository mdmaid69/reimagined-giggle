import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)