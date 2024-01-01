import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread