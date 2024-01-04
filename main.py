import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import shutil
def move_file(src, dst):
        shutil.move(src, dst)