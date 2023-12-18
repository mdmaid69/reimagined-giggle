import datetime
print(datetime.datetime.now())
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))