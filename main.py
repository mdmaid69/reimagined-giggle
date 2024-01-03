def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()