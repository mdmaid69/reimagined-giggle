import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()