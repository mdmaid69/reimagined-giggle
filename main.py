import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread