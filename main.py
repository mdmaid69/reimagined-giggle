import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def calculate_perpetuity(payment, rate):
        return payment / rate