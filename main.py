import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)