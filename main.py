def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()