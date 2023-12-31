import math
def calculate_logarithm_base_2(x):
        return math.log2(x)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)