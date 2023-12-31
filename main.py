import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)