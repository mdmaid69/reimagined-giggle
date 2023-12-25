import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b