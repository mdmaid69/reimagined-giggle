import shutil
def delete_directory(path):
        shutil.rmtree(path)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread