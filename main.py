def square_number(x):
        return x**2
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread