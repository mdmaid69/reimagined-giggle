import datetime
def get_today_date():
        return datetime.date.today()
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)