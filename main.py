def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)