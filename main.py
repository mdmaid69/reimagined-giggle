  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))