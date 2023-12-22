import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")