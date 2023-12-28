  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)