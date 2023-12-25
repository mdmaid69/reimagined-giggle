n = 10
print("Square numbers:", [x**2 for x in range(n)])
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread