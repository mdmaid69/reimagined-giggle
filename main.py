import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread