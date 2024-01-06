def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import time
def get_current_time():
        return time.time()