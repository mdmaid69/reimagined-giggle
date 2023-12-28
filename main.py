import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread