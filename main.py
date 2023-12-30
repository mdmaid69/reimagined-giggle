import re
def split_string(pattern, string):
        return re.split(pattern, string)
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)