import logging
def log_message(message):
        logging.info(message)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()