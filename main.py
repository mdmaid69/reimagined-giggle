import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def calculate_perimeter_triangle(a, b, c):
        return a + b + c