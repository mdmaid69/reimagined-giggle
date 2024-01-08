def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread