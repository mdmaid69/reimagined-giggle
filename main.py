import collections
def create_queue():
        return collections.deque()
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread