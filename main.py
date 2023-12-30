def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread