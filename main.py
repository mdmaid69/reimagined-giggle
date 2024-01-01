import datetime
def get_current_datetime():
        return datetime.datetime.now()
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time