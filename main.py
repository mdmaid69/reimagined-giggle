import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)