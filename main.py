import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread