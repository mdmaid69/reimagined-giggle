  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))