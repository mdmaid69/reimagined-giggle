import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)