import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
  def calculate_area_triangle(b, h):
        return 0.5 * b * h