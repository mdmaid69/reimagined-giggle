  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))