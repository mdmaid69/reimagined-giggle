  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread