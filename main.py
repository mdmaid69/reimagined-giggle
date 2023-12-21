import datetime
def get_current_datetime():
        return datetime.datetime.now()
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)