import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
  import numpy as np
  def calculate_median(arr):
        return np.median(arr)