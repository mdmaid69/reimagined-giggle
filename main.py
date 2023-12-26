import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time