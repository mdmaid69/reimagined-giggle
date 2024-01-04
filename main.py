import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
def calculate_work(force, distance):
        return force * distance