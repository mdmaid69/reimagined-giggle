import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import itertools
print(list(itertools.permutations([1, 2, 3])))