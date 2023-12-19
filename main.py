  import math
  def calculate_square_root(n):
        return math.sqrt(n)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread