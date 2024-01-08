import re
def split_string(pattern, string):
        return re.split(pattern, string)
def calculate_volume(length, width, height):
        return length * width * height