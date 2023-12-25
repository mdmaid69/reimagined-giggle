import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
def calculate_volume(length, width, height):
        return length * width * height