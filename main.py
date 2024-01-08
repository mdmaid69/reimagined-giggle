  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))