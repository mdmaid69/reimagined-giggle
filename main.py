import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)