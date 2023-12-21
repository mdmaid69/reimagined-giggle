import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
def calculate_volume(length, width, height):
        return length * width * height