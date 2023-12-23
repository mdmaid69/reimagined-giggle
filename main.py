def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())