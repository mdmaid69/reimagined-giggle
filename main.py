numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread