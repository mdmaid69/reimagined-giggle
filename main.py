  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))