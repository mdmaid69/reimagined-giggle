import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")