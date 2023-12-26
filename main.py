import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)