import datetime
def get_today_date():
        return datetime.date.today()
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)