import array
def iterate_over_array(array):
        for item in array:
        print(item)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)