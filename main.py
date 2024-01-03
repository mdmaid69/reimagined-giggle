  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread