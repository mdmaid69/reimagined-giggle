import os
def list_files_in_directory(path):
        return os.listdir(path)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)