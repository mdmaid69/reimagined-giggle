import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities