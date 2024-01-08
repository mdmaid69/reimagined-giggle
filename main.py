import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread