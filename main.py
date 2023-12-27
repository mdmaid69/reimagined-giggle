import array
def insert_into_array(array, i, item):
        array.insert(i, item)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)