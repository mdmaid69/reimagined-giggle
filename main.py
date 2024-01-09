import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import random
print(random.randint(0, 100))