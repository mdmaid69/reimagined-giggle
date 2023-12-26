import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()