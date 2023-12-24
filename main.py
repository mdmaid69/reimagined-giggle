import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
def is_even(n):
        return n % 2 == 0