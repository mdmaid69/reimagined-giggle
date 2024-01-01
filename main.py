  def calculate_circumference_circle(r):
        return 2 * 3.14 * r
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread