import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def convert_to_octal(n):
        return oct(n)