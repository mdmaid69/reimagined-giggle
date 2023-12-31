import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()