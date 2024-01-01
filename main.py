import array
def pop_from_array(array, i=-1):
        return array.pop(i)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)