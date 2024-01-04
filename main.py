  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)