import datetime
def get_current_date():
        return datetime.date.today()
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time