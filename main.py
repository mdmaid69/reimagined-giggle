import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import collections
def create_ordered_dict():
        return collections.OrderedDict()