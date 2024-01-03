  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))