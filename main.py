import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)