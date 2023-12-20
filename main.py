import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)