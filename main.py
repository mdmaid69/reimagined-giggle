import re
def split_string(pattern, string):
        return re.split(pattern, string)
def calculate_roi(gain, cost):
        return (gain - cost) / cost