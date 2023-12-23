import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))