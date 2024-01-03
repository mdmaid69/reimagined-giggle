def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import re
def split_string(pattern, string):
        return re.split(pattern, string)