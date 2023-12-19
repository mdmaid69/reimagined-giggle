import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets