  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)