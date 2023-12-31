import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)