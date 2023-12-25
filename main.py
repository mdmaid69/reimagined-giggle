  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)