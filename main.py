  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))