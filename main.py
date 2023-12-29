import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def calculate_perimeter_triangle(a, b, c):
        return a + b + c