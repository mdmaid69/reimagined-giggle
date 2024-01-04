import logging
def log_message(message):
        logging.info(message)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread