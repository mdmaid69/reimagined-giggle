import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))