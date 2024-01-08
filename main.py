import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import tensorflow as tf
print(tf.__version__)