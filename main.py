import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import numpy as np
print(np.array([1, 2, 3]))