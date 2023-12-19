def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import time
def get_time_since_epoch():
        return time.time()