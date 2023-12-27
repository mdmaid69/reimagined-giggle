  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)