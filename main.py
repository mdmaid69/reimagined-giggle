import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def convert_to_hex(n):
        return hex(n)