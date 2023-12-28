import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
  import os
  def split_path(path):
        return os.path.split(path)