import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]