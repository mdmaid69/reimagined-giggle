import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal