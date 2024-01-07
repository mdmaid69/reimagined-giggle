import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))