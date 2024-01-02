import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b