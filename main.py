import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)