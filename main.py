import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import glob
def find_files(pattern):
        return glob.glob(pattern)