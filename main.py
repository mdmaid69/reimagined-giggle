import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
n = 10
print("Powers of 2:", [2**x for x in range(n)])