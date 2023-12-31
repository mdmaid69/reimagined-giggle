  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)