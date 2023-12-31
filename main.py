  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()