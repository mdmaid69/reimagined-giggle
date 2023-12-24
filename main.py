import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)