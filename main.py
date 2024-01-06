import array
def convert_array_to_bytes(array):
        return array.tobytes()
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)