import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)