  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)