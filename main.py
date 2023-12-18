import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)