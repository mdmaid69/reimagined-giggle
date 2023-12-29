import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread