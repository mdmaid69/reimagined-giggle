import datetime
def get_today_date():
        return datetime.date.today()
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time