import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()