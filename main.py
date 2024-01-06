  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))