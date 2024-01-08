  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)