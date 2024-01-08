import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()