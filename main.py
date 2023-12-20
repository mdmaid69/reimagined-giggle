import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)