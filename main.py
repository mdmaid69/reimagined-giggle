import array
def get_array_as_bytearray(array):
        return bytearray(array)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)