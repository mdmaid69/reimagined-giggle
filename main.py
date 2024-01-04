  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))