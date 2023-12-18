import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread