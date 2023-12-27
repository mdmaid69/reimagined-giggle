import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def calculate_perpetuity(payment, rate):
        return payment / rate