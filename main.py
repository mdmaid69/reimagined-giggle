import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def convert_to_hex(n):
        return hex(n)