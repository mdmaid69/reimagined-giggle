import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def calculate_power(work, time):
        return work / time