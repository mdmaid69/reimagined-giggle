import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import time
print(time.time())