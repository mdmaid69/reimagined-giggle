import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)