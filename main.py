  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))