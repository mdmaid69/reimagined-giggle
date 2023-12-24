import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def calculate_roi(gain, cost):
        return (gain - cost) / cost