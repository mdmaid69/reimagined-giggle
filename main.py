import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def calculate_work(force, distance):
        return force * distance