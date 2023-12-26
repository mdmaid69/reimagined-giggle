for i in range(5):
        print(i)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread