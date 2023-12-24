  def convert_to_hex(n):
        return hex(n)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread