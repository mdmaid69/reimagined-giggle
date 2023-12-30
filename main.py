text = "Hello, world!"
print("Reversed:", text[::-1])
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread