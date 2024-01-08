def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import datetime
def get_current_datetime():
        return datetime.datetime.now()