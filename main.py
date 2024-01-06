  def multiply_numbers(x, y):
        return x * y
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread