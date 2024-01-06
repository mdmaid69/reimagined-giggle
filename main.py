  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()