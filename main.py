  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()