  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))