  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}