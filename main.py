  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread