import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)