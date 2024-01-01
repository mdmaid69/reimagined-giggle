import datetime
def get_today_date():
        return datetime.date.today()
def calculate_perpetuity(payment, rate):
        return payment / rate