import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps