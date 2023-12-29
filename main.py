import os
def get_environment_variable(var):
        return os.getenv(var)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread