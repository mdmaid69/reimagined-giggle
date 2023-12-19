import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)