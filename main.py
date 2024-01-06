  def calculate_area_circle(r):
        return 3.14 * r**2
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread