import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import logging
def setup_logging(level):
        logging.basicConfig(level=level)