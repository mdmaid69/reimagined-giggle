import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)