import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)