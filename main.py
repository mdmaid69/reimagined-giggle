def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)