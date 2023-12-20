import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time