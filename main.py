import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()