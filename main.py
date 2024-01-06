def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)