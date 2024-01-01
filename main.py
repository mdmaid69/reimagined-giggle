import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def calculate_speed(distance, time):
        return distance / time