import array
def get_array_buffer_info(array):
        return array.buffer_info()
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)