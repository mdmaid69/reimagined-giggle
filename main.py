import math
def calculate_hyperbolic_cosine(x):
        return math.cosh(x)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)