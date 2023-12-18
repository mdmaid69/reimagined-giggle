import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread