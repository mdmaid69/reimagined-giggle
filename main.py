import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)