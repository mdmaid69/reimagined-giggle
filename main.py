def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
import re
def split_string(pattern, string):
        return re.split(pattern, string)