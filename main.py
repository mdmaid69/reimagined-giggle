def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()