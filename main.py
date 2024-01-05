import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)