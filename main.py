import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def calculate_roi(gain, cost):
        return (gain - cost) / cost