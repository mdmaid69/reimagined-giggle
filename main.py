  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)