def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import time
def get_time_since_epoch():
        return time.time()