import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue