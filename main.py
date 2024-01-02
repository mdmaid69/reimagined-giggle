import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)