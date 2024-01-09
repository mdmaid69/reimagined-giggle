import re
print(re.match("h.*o", "hello world"))
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time