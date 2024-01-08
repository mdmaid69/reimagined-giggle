  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))