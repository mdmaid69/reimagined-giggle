import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import logging
def setup_logging(level):
        logging.basicConfig(level=level)