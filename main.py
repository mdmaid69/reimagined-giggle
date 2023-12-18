  def calculate_perimeter_triangle(a, b, c):
        return a + b + c
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread