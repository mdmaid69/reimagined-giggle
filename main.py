import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding