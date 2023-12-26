  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread