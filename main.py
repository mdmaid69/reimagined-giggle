  def is_odd(n):
        return n % 2 != 0
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread