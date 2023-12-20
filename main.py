  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread