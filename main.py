def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)