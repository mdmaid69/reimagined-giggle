import collections
def create_counter():
        return collections.Counter()
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread