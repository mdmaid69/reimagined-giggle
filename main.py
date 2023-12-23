import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)