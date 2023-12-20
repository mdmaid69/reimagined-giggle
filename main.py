import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
n = 10
print("Cube numbers:", [x**3 for x in range(n)])