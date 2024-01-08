  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()