import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
print([x**2 for x in range(10)])