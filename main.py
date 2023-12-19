import datetime
def get_current_datetime():
        return datetime.datetime.now()
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal