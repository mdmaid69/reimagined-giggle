import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)