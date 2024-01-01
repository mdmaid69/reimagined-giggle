import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)