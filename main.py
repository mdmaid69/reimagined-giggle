  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))