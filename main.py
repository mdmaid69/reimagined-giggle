import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def calculate_area(radius):
        return 3.14 * radius * radius