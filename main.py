import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def calculate_area(radius):
        return 3.14 * radius * radius