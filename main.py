import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)