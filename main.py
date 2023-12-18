  def calculate_area_rectangle(l, w):
        return l * w
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread