import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))