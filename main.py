import sys
print(sys.version)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread