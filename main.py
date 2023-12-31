import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def calculate_roi(gain, cost):
        return (gain - cost) / cost