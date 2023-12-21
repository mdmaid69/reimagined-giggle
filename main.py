def calculate_roi(gain, cost):
        return (gain - cost) / cost
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()