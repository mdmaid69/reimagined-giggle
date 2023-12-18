import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity