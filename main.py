import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
for i in range(10): print(i)