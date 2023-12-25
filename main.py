i = 0
while i < 5:
        print(i)
        i += 1
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread