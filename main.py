import random
print(random.randint(0, 100))
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread