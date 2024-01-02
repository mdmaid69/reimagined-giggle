def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()