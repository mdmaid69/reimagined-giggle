  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))