import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)