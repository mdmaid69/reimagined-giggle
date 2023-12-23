import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()