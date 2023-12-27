  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import math
def calculate_sign(x):
        return math.copysign(1, x)