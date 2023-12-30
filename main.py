  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread