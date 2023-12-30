def calculate_average(lst):
        return sum(lst) / len(lst)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()