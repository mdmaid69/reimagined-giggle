import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)