import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)