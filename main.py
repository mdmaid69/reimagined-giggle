def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import re
def split_string(pattern, string):
        return re.split(pattern, string)