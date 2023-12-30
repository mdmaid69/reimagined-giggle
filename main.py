def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import re
def split_string(pattern, string):
        return re.split(pattern, string)