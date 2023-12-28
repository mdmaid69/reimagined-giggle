  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)