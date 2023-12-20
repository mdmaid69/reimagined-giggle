  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())