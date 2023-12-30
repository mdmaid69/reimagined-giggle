import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities