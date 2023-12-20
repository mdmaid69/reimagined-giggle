def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread