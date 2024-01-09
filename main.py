import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)