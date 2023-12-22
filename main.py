import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
def calculate_perpetuity(payment, rate):
        return payment / rate