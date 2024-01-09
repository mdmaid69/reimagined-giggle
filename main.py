import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time