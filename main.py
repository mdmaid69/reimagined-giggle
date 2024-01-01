  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns