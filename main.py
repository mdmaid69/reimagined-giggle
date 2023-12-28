def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)